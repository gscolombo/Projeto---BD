from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from repositories.ocurrences import *
from repositories.dto import OcorrenciaDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/ocorrencias", tags=["Ocorrência"])

class OcorrenciaCreate(BaseModel):
    ocurrence: Ocorrencia
    kind: str
    details: dict

@router.get("")
def get_ocurrences():
    return list_ocurrences()

@router.get("/{id}")
def get_ocurrence_by_id(id: int):
    o = find_ocurrence_by_id(id)
    if o:
        return o
    raise HTTPException(status_code=404, detail="Ocorrência não encontrada.")

@router.get("/veiculo/{placa_veiculo}")
def get_ocurrences_by_veiculo(placa_veiculo: str):
    ocurrences = find_ocurrences_by_veiculo(placa_veiculo)
    if ocurrences:
        return ocurrences
    raise HTTPException(status_code=404, detail="Ocorrências não encontradas para o veículo.")

@router.post("", status_code=201)
def post_ocurrence(ocurrence_data: OcorrenciaCreate):
    try:
        id = create_ocurrence(ocurrence_data.ocurrence, ocurrence_data.kind, ocurrence_data.details)
        return {"id": id}
    except Exception as e:
        raise CustomHTTPException(400, "Erro durante processamento de consulta", str(e))

@router.put("/{id}")
def put_ocurrence(id: int, ocurrence: OcorrenciaDTO):
    try:
        o = update_ocurrence(id, ocurrence)
        if o:
            return o
        raise HTTPException(status_code=404, detail="Ocorrência não encontrada.")
    except Exception as e:
        raise CustomHTTPException(400, "Erro durante processamento de consulta", str(e))

@router.delete("/{id}")
def delete_ocurrence(id: int):
    try:
        ok = remove_ocurrence(id)
        if ok:
            return {"ok": ok}
        raise HTTPException(status_code=404, detail="Ocorrência não encontrada.")
    except Exception as e:
        raise CustomHTTPException(400, "Erro durante processamento de consulta", str(e))