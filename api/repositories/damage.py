from sqlmodel import Session, select

from db.engine import engine
from db.models import Avaria
from repositories.dto import AvariaDTO

def list_damages() -> list:
    with Session(engine) as session:
        stmt = select(Avaria)
        results = session.exec(stmt)
        return [dict(a) for a in results]

def find_damage_by_id(id_ocorrencia: int) -> dict | None:
    with Session(engine) as session:
        a = session.get(Avaria, id_ocorrencia)
        if a:
            return dict(a)

def create_damage(damage: Avaria) -> int:
    with Session(engine) as session:
        session.add(damage)
        session.commit()
        return damage.id_ocorrencia

def update_damage(id_ocorrencia: int, damage: AvariaDTO) -> Avaria | None:
    with Session(engine) as session:
        a = session.get(Avaria, id_ocorrencia)
        if a:
            damage_data = damage.model_dump(exclude_unset=True)
            a.sqlmodel_update(damage_data)
            session.add(a)
            session.commit()
            session.refresh(a)
            return a

def remove_damage(id_ocorrencia: int) -> bool | None:
    with Session(engine) as session:
        a = session.get(Avaria, id_ocorrencia)
        if a:
            session.delete(a)
            session.commit()
            return True