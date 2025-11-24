from sqlmodel import Session, select

from db.engine import engine
from db.models import Linha
from repositories.dto import LinhaDTO


def list_lines() -> list:
    with Session(engine) as session:
        stmt = select(Linha)
        results = session.exec(stmt)
        return [dict(l) for l in results]


def find_line_by_code(codigo: str) -> dict | None:
    with Session(engine) as session:
        l = session.get(Linha, codigo)
        if l:
            return dict(l)


def create_line(line: Linha) -> str:
    with Session(engine) as session:
        session.add(line)
        session.commit()
        return line.codigo


def update_line(codigo: str, line: LinhaDTO) -> Linha | None:
    with Session(engine) as session:
        l = session.get(Linha, codigo)
        if l:
            line_data = line.model_dump(exclude_unset=True)
            l.sqlmodel_update(line_data)
            session.add(l)
            session.commit()
            session.refresh(l)
            return l


def remove_line(codigo: str) -> bool | None:
    with Session(engine) as session:
        l = session.get(Linha, codigo)
        if l:
            session.delete(l)
            session.commit()
            return True
