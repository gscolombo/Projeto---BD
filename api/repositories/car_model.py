from sqlmodel import Session, select

from db.engine import engine
from db.models import Modelo
from repositories.dto import ModeloDTO

def list_models() -> list:
    with Session(engine) as session:
        stmt = select(Modelo)
        results = session.exec(stmt)
        return [dict(m) for m in results]

def find_model_by_id(codigo: int) -> dict | None:
    with Session(engine) as session:
        m = session.get(Modelo, codigo)
        if m:
            return dict(m)

def create_model(model: Modelo) -> int:
    with Session(engine) as session:
        session.add(model)
        session.commit()
        session.refresh(model)
        return model.codigo

def update_model(codigo: int, model: ModeloDTO) -> Modelo | None:
    with Session(engine) as session:
        m = session.get(Modelo, codigo)
        if m:
            model_data = model.model_dump(exclude_unset=True)
            m.sqlmodel_update(model_data)
            session.add(m)
            session.commit()
            session.refresh(m)
            return m

def remove_model(codigo: int) -> bool | None:
    with Session(engine) as session:
        m = session.get(Modelo, codigo)
        if m:
            session.delete(m)
            session.commit()
            return True