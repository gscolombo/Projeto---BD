from sqlmodel import Session, select, or_, Sequence

from db.engine import engine
from db.models import Local
from repositories.dto import LocalDTO


def find_all_locals() -> Sequence[Local]:
    with Session(engine) as session:
        return session.exec(select(Local)).fetchall()


def find_locals_by(lat: str, lng: str, nome: str, descricao: str) -> Sequence[Local]:
    with Session(engine) as session:
        stmt = select(Local) \
            .where(or_(Local.lat == lat,
                       Local.lng == lng,
                       Local.nome.like(f"%{nome}%"),
                       Local.descricao.like(f"%{descricao}%")))

        return session.exec(stmt).fetchall()


def create_local(local: Local) -> tuple[float]:
    with Session(engine) as session:
        session.add(local)
        session.commit()
        return local.lat, local.lng


def update_local(lat: str, lng: str, local: LocalDTO) -> Local:
    with Session(engine) as session:
        pass


def remove_local(lat: str, lng: str) -> bool | None:
    with Session(engine) as session:
        pass
