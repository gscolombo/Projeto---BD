from sqlmodel import Session, select

from db.engine import engine
from db.models import Manutencao
from repositories.dto import ManutencaoDTO

def list_maintenances() -> list:
    with Session(engine) as session:
        stmt = select(Manutencao)
        results = session.exec(stmt)
        return [dict(m) for m in results]

def find_maintenance_by_id(id: int) -> dict | None:
    with Session(engine) as session:
        m = session.get(Manutencao, id)
        if m:
            return dict(m)

def create_maintenance(maintenance: Manutencao) -> int:
    with Session(engine) as session:
        session.add(maintenance)
        session.commit()
        session.refresh(maintenance)
        return maintenance.id

def update_maintenance(id: int, maintenance: ManutencaoDTO) -> Manutencao | None:
    with Session(engine) as session:
        m = session.get(Manutencao, id)
        if m:
            maintenance_data = maintenance.model_dump(exclude_unset=True)
            m.sqlmodel_update(maintenance_data)
            session.add(m)
            session.commit()
            session.refresh(m)
            return m

def remove_maintenance(id: int) -> bool | None:
    with Session(engine) as session:
        m = session.get(Manutencao, id)
        if m:
            session.delete(m)
            session.commit()
            return True