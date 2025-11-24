from sqlmodel import Session, select

from db.engine import engine
from db.models import Motorista, Funcionario
from repositories.dto import MotoristaDTO

def list_drivers() -> list:
    with Session(engine) as session:
        stmt = select(Motorista)
        results = session.exec(stmt)
        return [dict(m) for m in results]

def find_driver_by_cnh(cnh: str) -> dict | None:
    with Session(engine) as session:
        m = session.get(Motorista, cnh)
        if m:
            return dict(m)

def find_driver_by_employee(codigo_funcionario: int) -> dict | None:
    with Session(engine) as session:
        stmt = select(Motorista).where(Motorista.codigo_funcionario == codigo_funcionario)
        m = session.exec(stmt).first()
        if m:
            return dict(m)

def create_driver(driver: Motorista) -> str:
    with Session(engine) as session:
        session.add(driver)
        session.commit()
        return driver.cnh

def update_driver(cnh: str, driver: MotoristaDTO) -> Motorista | None:
    with Session(engine) as session:
        m = session.get(Motorista, cnh)
        if m:
            driver_data = driver.model_dump(exclude_unset=True)
            m.sqlmodel_update(driver_data)
            session.add(m)
            session.commit()
            session.refresh(m)
            return m

def remove_driver(cnh: str) -> bool | None:
    with Session(engine) as session:
        m = session.get(Motorista, cnh)
        if m:
            session.delete(m)
            session.commit()
            return True