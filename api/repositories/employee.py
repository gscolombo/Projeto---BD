from sqlmodel import Session, select

from db.engine import engine
from db.models import Funcionario
from repositories.dto import FuncionarioDTO


def list_employees() -> list:
    with Session(engine) as session:
        stmt = select(Funcionario)

        results = session.exec(stmt)

        return [
            {
                **dict(f),
                "telefones": [t.telefone for t in f.telefones]
            }
            for f in results
        ]


def find_employee_by_id(codigo: int) -> dict | None:
    with Session(engine) as session:
        f = session.get(Funcionario, codigo)

        if (f):  # Include telephones
            df = dict(f)
            df["telefones"] = [t.telefone for t in f.telefones]

            return df


def find_employee_by_name(name: str) -> list | None:
    with Session(engine) as session:
        stmt = select(Funcionario).where(Funcionario.nome.like(f"%{name}%")) # type: ignore

        results = session.exec(stmt).fetchall()
        if (len(results)):
            return [
                {
                    **dict(f),
                    "telefones": [t.telefone for t in f.telefones]
                }
                for f in results
            ]


def create_employee(employee: Funcionario) -> int:
    with Session(engine) as session:
        session.add(employee)
        session.commit()
        session.refresh(employee)

        return employee.codigo


def update_employee(codigo: int, employee: FuncionarioDTO) -> Funcionario | None:
    with Session(engine) as session:
        w = session.get(Funcionario, codigo)
        if w:
            employee_data = employee.model_dump(exclude_unset=True)
            w.sqlmodel_update(employee_data)
            session.add(w)
            session.commit()
            session.refresh(w)
            return w


def remove_employee(codigo: int):
    with Session(engine) as session:
        w = session.get(Funcionario, codigo)
        if w:
            session.delete(w)
            session.commit()
            return True
