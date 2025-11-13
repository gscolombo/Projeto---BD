from fastapi import APIRouter, HTTPException

from repositories.car_model import *
from repositories.dto import ModeloDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/modelo", tags=["Modelo"])


@router.get("")
def get_models():
    return list_models()


@router.get("/{codigo}")
def get_model_by_id(codigo: int):
    m = find_model_by_id(codigo)
    if m:
        return m
    raise HTTPException(status_code=404, detail="Modelo não encontrado.")


@router.post("", status_code=201)
def post_model(model: Modelo):
    try:
        codigo = create_model(model)
        return {"codigo": codigo}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{codigo}")
def put_model(codigo: int, model: ModeloDTO):
    try:
        m = update_model(codigo, model)
        if m:
            return m
        raise HTTPException(status_code=404, detail="Modelo não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{codigo}")
def delete_model(codigo: int):
    try:
        ok = remove_model(codigo)
        if ok:
            return {"ok": ok}
        raise HTTPException(status_code=404, detail="Modelo não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
