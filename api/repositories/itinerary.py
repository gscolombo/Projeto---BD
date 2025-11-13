from sqlmodel import Session, select

from db.engine import engine
from db.models import Itinerario
from repositories.dto import ItinerarioDTO


def list_itineraries() -> list:
    with Session(engine) as session:
        stmt = select(Itinerario)
        results = session.exec(stmt)
        return [dict(i) for i in results]


def find_itinerary_by_line(codigo_linha: str) -> list:
    with Session(engine) as session:
        stmt = select(Itinerario) \
            .where(Itinerario.codigo_linha == codigo_linha) \
            .order_by(Itinerario.numero)

        results = session.exec(stmt)
        return [dict(i) for i in results]


def create_itinerary(itinerary: Itinerario) -> Itinerario:
    with Session(engine) as session:
        session.add(itinerary)
        session.commit()
        return itinerary


def update_itinerary(codigo_linha: str, lat_local: float, lng_local: float, numero: int, itinerario: ItinerarioDTO) -> Itinerario | None:
    with Session(engine) as session:
        i = session.get(Itinerario,
                        (codigo_linha, lat_local, lng_local, numero))
        if i:
            itinerary_data = itinerario.model_dump(exclude_unset=True)
            i.sqlmodel_update(itinerary_data)
            session.add(i)
            session.commit()
            session.refresh(i)
            return i


def remove_itinerary(codigo_linha: str, lat_local: float, lng_local: float, numero: int) -> bool | None:
    with Session(engine) as session:
        i = session.get(Itinerario,
                        (codigo_linha, lat_local, lng_local, numero))
        if i:
            session.delete(i)
            session.commit()
            return True
