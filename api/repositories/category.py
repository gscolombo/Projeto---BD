from sqlmodel import Session, select

from db.engine import engine
from db.models import Categoria
from repositories.dto import CategoriaDTO

def list_categories() -> list:
    with Session(engine) as session:
        stmt = select(Categoria)
        results = session.exec(stmt)
        return [dict(c) for c in results]

def find_category_by_id(codigo: int) -> dict | None:
    with Session(engine) as session:
        c = session.get(Categoria, codigo)
        if c:
            return dict(c)

def create_category(category: Categoria) -> int:
    with Session(engine) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category.codigo

def update_category(codigo: int, category: CategoriaDTO) -> Categoria | None:
    with Session(engine) as session:
        c = session.get(Categoria, codigo)
        if c:
            category_data = category.model_dump(exclude_unset=True)
            c.sqlmodel_update(category_data)
            session.add(c)
            session.commit()
            session.refresh(c)
            return c

def remove_category(codigo: int) -> bool | None:
    with Session(engine) as session:
        c = session.get(Categoria, codigo)
        if c:
            session.delete(c)
            session.commit()
            return True