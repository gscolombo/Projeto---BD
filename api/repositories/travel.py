from sqlmodel import Session, select
from datetime import date, datetime

from db.engine import engine
from db.models import Viagem
from repositories.dto import ViagemDTO


def list_travels() -> list:
    with Session(engine) as session:
        stmt = select(Viagem)
        results = session.exec(stmt)
        return [dict(v) for v in results]


def find_travel(codigo_linha: str, codigo_cobrador: int, codigo_motorista:
                      int, placa_veiculo: str, data: date, hora_partida: datetime) -> dict | None:
    with Session(engine) as session:
        v = session.get(Viagem, (codigo_linha, codigo_cobrador,
                        codigo_motorista, placa_veiculo, data, hora_partida))
        if v:
            return dict(v)


def create_travel(travel: Viagem) -> tuple:
    with Session(engine) as session:
        session.add(travel)
        session.commit()
        return (travel.codigo_linha, travel.codigo_cobrador, travel.codigo_motorista,
                travel.placa_veiculo, travel.data, travel.hora_partida)


def update_travel(codigo_linha: str, codigo_cobrador: int, codigo_motorista: int,
                  placa_veiculo: str, data: date, hora_partida: datetime, travel: ViagemDTO) -> Viagem | None:
    with Session(engine) as session:
        v = session.get(Viagem, (codigo_linha, codigo_cobrador,
                        codigo_motorista, placa_veiculo, data, hora_partida))
        if v:
            travel_data = travel.model_dump(exclude_unset=True)
            v.sqlmodel_update(travel_data)
            session.add(v)
            session.commit()
            session.refresh(v)
            return v


def remove_travel(codigo_linha: str, codigo_cobrador: int, codigo_motorista: int,
                  placa_veiculo: str, data: date, hora_partida: datetime) -> bool | None:
    with Session(engine) as session:
        v = session.get(Viagem, (codigo_linha, codigo_cobrador,
                        codigo_motorista, placa_veiculo, data, hora_partida))
        if v:
            session.delete(v)
            session.commit()
            return True
