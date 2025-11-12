from sqlmodel import Session, select

from db.engine import engine
from db.models import Funcionario


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
        stmt = select(Funcionario).where(Funcionario.codigo == codigo)
        f = session.exec(stmt).first()

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
