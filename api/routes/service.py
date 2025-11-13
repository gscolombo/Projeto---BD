from fastapi import APIRouter, HTTPException

from repositories.service import *
from repositories.dto import ServicoDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/servico", tags=["Serviço"])


@router.get("")
def get_services():
    return list_services()


@router.get("/{codigo}")
def get_service_by_id(codigo: int):
    s = find_service_by_id(codigo)
    if s:
        return s
    raise HTTPException(status_code=404, detail="Serviço não encontrado.")


@router.post("", status_code=201)
def post_service(service: Servico):
    try:
        codigo = create_service(service)
        return {"codigo": codigo}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{codigo}")
def put_service(codigo: int, service: ServicoDTO):
    try:
        s = update_service(codigo, service)
        if s:
            return s
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{codigo}")
def delete_service(codigo: int):
    try:
        ok = remove_service(codigo)
        if ok:
            return {"ok": ok}
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
