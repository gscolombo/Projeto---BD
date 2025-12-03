from sqlmodel import Session, select, or_, text
import json

from db.engine import engine
from db.models import Empresa
from db.procedures import NewCompanyData

from repositories.dto import EmpresaDTO


def get_company_data() -> list:
    with Session(engine) as session:
        stmt = select(Empresa)
        results = session.exec(stmt)

        return [  # Append associated data
            {
                **dict(e),
                "funcionarios": [{
                    **dict(f),
                    "telefones": [t.telefone for t in f.telefones]

                } for f in e.funcionarios],
                "veiculos": [{
                    **dict(v),
                    "ocorrencias": [o for o in v.ocorrencias]

                } for v in e.veiculos],
                "linhas": e.linhas
            }
            for e in results
        ]


def find_company(cnpj: str = None, company_name: str = None, trade_name: str = None) -> dict | None:
    with Session(engine) as session:
        stmt = select(Empresa).where(or_(Empresa.cnpj == cnpj,
                                         Empresa.razao_social == company_name,
                                         Empresa.nome_fantasia == trade_name))
        result = session.exec(stmt).fetchall()

        if (len(result)):  # Append associated data
            return [
                {
                    **dict(e),
                    "funcionarios": [{
                        **dict(f),
                        "telefones": [t.telefone for t in f.telefones]

                    } for f in e.funcionarios],
                    "veiculos": e.veiculos,
                }
                for e in result
            ]


def create_company(company: Empresa) -> str:
    with Session(engine) as session:
        session.add(company)
        session.commit()

        return company.cnpj


def update_company(cnpj: str, company: EmpresaDTO) -> Empresa | None:
    with Session(engine) as session:
        c = session.get(Empresa, cnpj)
        if c:
            company_data = company.model_dump(exclude_unset=True, exclude_none=True)
            c.sqlmodel_update(company_data)
            session.add(c)
            session.commit()
            session.refresh(c)
            return c


def remove_company(cnpj: str) -> bool | None:
    with Session(engine) as session:
        try:
            query = text("CALL delete_company(:cnpj)")
            session.exec(query, params={"cnpj": cnpj})
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        
# Procedures
def save_new_company(data: NewCompanyData):
    with Session(engine) as session:
        try:
            query = text("""CALL save_new_company(
                            :cnpj,
                            :razao_social,
                            :nome_fantasia,
                            :lat_local,
                            :lng_local,
                            :local_nome,
                            :local_descricao,
                            :employees,
                            :vehicles
                        );
                        """)

            session.exec(query, params={
                "cnpj": data.cnpj,
                "razao_social": data.razao_social,
                "nome_fantasia": data.nome_fantasia,
                "lat_local": data.lat_local,
                "lng_local": data.lng_local,
                "local_nome": data.local_nome,
                "local_descricao": data.local_descricao,
                "employees": json.dumps([e.model_dump() for e in data.employees]),
                "vehicles": json.dumps([v.model_dump() for v in data.vehicles])
            })

            session.commit()
        except Exception as e:
            session.rollback()
            raise e