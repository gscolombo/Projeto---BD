from sqlmodel import Session, select

from db.engine import engine
from db.models import Manutencao_Servico


def list_maintenance_services() -> list:
    with Session(engine) as session:
        stmt = select(Manutencao_Servico)
        results = session.exec(stmt)
        return [dict(ms) for ms in results]


def find_services_by_maintenance(id_maintenance: int) -> list:
    with Session(engine) as session:
        stmt = select(Manutencao_Servico).where(
            Manutencao_Servico.id_manutencao == id_maintenance)
        results = session.exec(stmt)
        return [dict(ms) for ms in results]


def create_maintenance_service(maintenance_service: Manutencao_Servico) -> tuple:
    with Session(engine) as session:
        session.add(maintenance_service)
        session.commit()
        return maintenance_service.id_manutencao, maintenance_service.codigo_servico


def remove_maintenance_service(id_maintenance: int, codigo_service: int) -> bool | None:
    with Session(engine) as session:
        ms = session.get(Manutencao_Servico, (id_maintenance, codigo_service))
        if ms:
            session.delete(ms)
            session.commit()
            return True
