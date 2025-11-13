from sqlmodel import Session, select

from db.engine import engine
from db.models import Servico
from repositories.dto import ServicoDTO

def list_services() -> list:
    with Session(engine) as session:
        stmt = select(Servico)
        results = session.exec(stmt)
        return [dict(s) for s in results]

def find_service_by_id(codigo: int) -> dict | None:
    with Session(engine) as session:
        s = session.get(Servico, codigo)
        if s:
            return dict(s)

def create_service(service: Servico) -> int:
    with Session(engine) as session:
        session.add(service)
        session.commit()
        session.refresh(service)
        return service.codigo

def update_service(codigo: int, service: ServicoDTO) -> Servico | None:
    with Session(engine) as session:
        s = session.get(Servico, codigo)
        if s:
            service_data = service.model_dump(exclude_unset=True)
            s.sqlmodel_update(service_data)
            session.add(s)
            session.commit()
            session.refresh(s)
            return s

def remove_service(codigo: int) -> bool | None:
    with Session(engine) as session:
        s = session.get(Servico, codigo)
        if s:
            session.delete(s)
            session.commit()
            return True