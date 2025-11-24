from sqlmodel import Session, select

from db.engine import engine
from db.models import Acidente
from repositories.dto import AcidenteDTO

def list_accidents() -> list:
    with Session(engine) as session:
        stmt = select(Acidente)
        results = session.exec(stmt)
        return [dict(a) for a in results]

def find_accident_by_id(id_ocorrencia: int) -> dict | None:
    with Session(engine) as session:
        a = session.get(Acidente, id_ocorrencia)
        if a:
            return dict(a)

def create_accident(accident: Acidente) -> int:
    with Session(engine) as session:
        session.add(accident)
        session.commit()
        return accident.id_ocorrencia

def update_accident(id_ocorrencia: int, accident: AcidenteDTO) -> Acidente | None:
    with Session(engine) as session:
        a = session.get(Acidente, id_ocorrencia)
        if a:
            accident_data = accident.model_dump(exclude_unset=True)
            a.sqlmodel_update(accident_data)
            session.add(a)
            session.commit()
            session.refresh(a)
            return a

def remove_accident(id_ocorrencia: int) -> bool | None:
    with Session(engine) as session:
        a = session.get(Acidente, id_ocorrencia)
        if a:
            session.delete(a)
            session.commit()
            return True