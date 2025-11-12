from sqlmodel import Session, select

from db.engine import engine
from db.models import Funcionario
from repositories.dto import FuncionarioDTO


def list_workers() -> list:
    with Session(engine) as session:
        stmt = select(Funcionario)

        results = session.exec(stmt)

        return [
            {
                **f.__dict__,
                "telefones": [t.telefone for t in f.telefones]
            }
            for f in results
        ]


def find_worker_by_id(codigo: int) -> dict | None:
    with Session(engine) as session:
        f = session.get(Funcionario, codigo)

        if (f):  # Include telephones
            df = dict(f)
            df["telefones"] = [t.telefone for t in f.telefones]

            return df


def find_worker_by_name(name: str) -> dict | None:
    with Session(engine) as session:
        stmt = select(Funcionario).where(Funcionario.nome.like(f"%{name}%"))

        results = session.exec(stmt).fetchall()
        if (len(results)):
            return [
                {
                    **f.__dict__,
                    "telefones": [t.telefone for t in f.telefones]
                }
                for f in results
            ]

def create_worker(worker: Funcionario) -> int:
    with Session(engine) as session:
        session.add(worker)
        session.commit()
        session.refresh(worker)

        return worker.codigo

def update_worker(codigo: int, worker: FuncionarioDTO) -> Funcionario | None:
    with Session(engine) as session:
        w = session.get(Funcionario, codigo)    
        if w:
            worker_data = worker.model_dump(exclude_unset=True)
            w.sqlmodel_update(worker_data)
            session.add(w)
            session.commit()
            session.refresh(w)
            return w