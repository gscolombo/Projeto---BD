from fastapi import APIRouter, HTTPException

from repositories.category import *
from repositories.dto import CategoriaDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/categoria", tags=["Categoria"])


@router.get("")
def get_categories():
    return list_categories()


@router.get("/{codigo}")
def get_category_by_id(codigo: int):
    c = find_category_by_id(codigo)
    if c:
        return c
    raise HTTPException(status_code=404, detail="Categoria não encontrada.")


@router.post("", status_code=201)
def post_category(category: Categoria):
    try:
        codigo = create_category(category)
        return {"codigo": codigo}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{codigo}")
def put_category(codigo: int, category: CategoriaDTO):
    try:
        c = update_category(codigo, category)
        if c:
            return c
        raise HTTPException(
            status_code=404, detail="Categoria não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{codigo}")
def delete_category(codigo: int):
    try:
        ok = remove_category(codigo)
        if ok:
            return {"ok": ok}
        raise HTTPException(
            status_code=404, detail="Categoria não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
