from sqlmodel import Session, select

from db.engine import engine
from db.models import Ocorrencia, Acidente, Avaria
from repositories.dto import OcorrenciaDTO


def list_ocurrences() -> list:
    with Session(engine) as session:
        stmt = select(Ocorrencia)
        results = session.exec(stmt)
        return [dict(o) for o in results]


def find_ocurrence_by_id(id: int) -> dict | None:
    with Session(engine) as session:
        o = session.get(Ocorrencia, id)
        if o:
            ocurrence_data = dict(o)

            accident = session.get(Acidente, id)
            damage = session.get(Avaria, id)

            if accident:
                ocurrence_data["kind"] = "accident"
                ocurrence_data.update(dict(accident))
            elif damage:
                ocurrence_data["kind"] = "damage"
                ocurrence_data.update(dict(damage))

            return ocurrence_data


def find_ocurrences_by_veiculo(placa_veiculo: str) -> list:
    with Session(engine) as session:
        stmt = select(Ocorrencia).where(
            Ocorrencia.placa_veiculo == placa_veiculo)
        results = session.exec(stmt)
        return [dict(o) for o in results]


def create_ocurrence(ocurrence: Ocorrencia, tipo: str, detalhes: dict) -> int:
    with Session(engine) as session:
        session.add(ocurrence)
        session.commit()
        session.refresh(ocurrence)

        if tipo == "accident":
            accident = Acidente(id_ocurrence=ocurrence.id, **detalhes)
            session.add(accident)
        elif tipo == "damage":
            damage = Avaria(id_ocurrence=ocurrence.id, **detalhes)
            session.add(damage)

        session.commit()
        return ocurrence.id


def update_ocurrence(id: int, ocurrence: OcorrenciaDTO) -> Ocorrencia | None:
    with Session(engine) as session:
        o = session.get(Ocorrencia, id)
        if o:
            ocurrence_data = ocurrence.model_dump(exclude_unset=True)
            o.sqlmodel_update(ocurrence_data)
            session.add(o)
            session.commit()
            session.refresh(o)
            return o


def remove_ocurrence(id: int) -> bool | None:
    with Session(engine) as session:
        o = session.get(Ocorrencia, id)
        if o:
            session.delete(o)
            session.commit()
            return True
