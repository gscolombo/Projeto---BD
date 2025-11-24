from fastapi import APIRouter, HTTPException

from repositories.line import *
from repositories.dto import LinhaDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/linha", tags=["Linha"])


@router.get("")
def get_lines():
    return list_lines()


@router.get("/{codigo}")
def get_line_by_code(codigo: str):
    l = find_line_by_code(codigo)
    if l:
        return l
    raise HTTPException(status_code=404, detail="Linha não encontrada.")


@router.post("", status_code=201)
def post_line(linha: Linha):
    try:
        codigo = create_line(linha)
        return {"codigo": codigo}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{codigo}")
def put_line(codigo: str, linha: LinhaDTO):
    try:
        l = update_line(codigo, linha)
        if l:
            return l
        raise HTTPException(status_code=404, detail="Linha não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{codigo}")
def delete_line(codigo: str):
    try:
        ok = remove_line(codigo)
        if ok:
            return {"ok": ok}
        raise HTTPException(status_code=404, detail="Linha não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
