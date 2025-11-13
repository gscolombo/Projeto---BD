from sqlmodel import Session, select

from db.engine import engine
from db.models import Veiculo
from repositories.dto import VeiculoDTO

def list_vehicles() -> list:
    with Session(engine) as session:
        stmt = select(Veiculo)
        results = session.exec(stmt)
        return [dict(v) for v in results]

def find_vehicle_by_placa(placa: str) -> dict | None:
    with Session(engine) as session:
        v = session.get(Veiculo, placa)
        if v:
            return dict(v)

def find_vehicles_by_company(cnpj: str) -> list:
    with Session(engine) as session:
        stmt = select(Veiculo).where(Veiculo.cnpj_empresa == cnpj)
        results = session.exec(stmt)
        return [dict(v) for v in results]

def create_vehicle(vehicle: Veiculo) -> str:
    with Session(engine) as session:
        session.add(vehicle)
        session.commit()
        return vehicle.placa

def update_vehicle(placa: str, vehicle: VeiculoDTO) -> Veiculo | None:
    with Session(engine) as session:
        v = session.get(Veiculo, placa)
        if v:
            vehicle_data = vehicle.model_dump(exclude_unset=True)
            v.sqlmodel_update(vehicle_data)
            session.add(v)
            session.commit()
            session.refresh(v)
            return v

def remove_vehicle(placa: str) -> bool | None:
    with Session(engine) as session:
        v = session.get(Veiculo, placa)
        if v:
            session.delete(v)
            session.commit()
            return True