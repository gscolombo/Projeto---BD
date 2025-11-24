from fastapi import APIRouter, HTTPException

from repositories.accident import *
from repositories.dto import AcidenteDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/acidente", tags=["Acidente"])


@router.get("")
def get_accidents():
    return list_accidents()


@router.get("/{id_ocorrencia}")
def get_accident_by_id(id_ocorrencia: int):
    a = find_accident_by_id(id_ocorrencia)
    if a:
        return a
    raise HTTPException(status_code=404, detail="Acidente não encontrado.")


@router.post("", status_code=201)
def post_accident(accident: Acidente):
    try:
        id = create_accident(accident)
        return {"id_ocorrencia": id}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{id_ocorrencia}")
def put_accident(id_ocorrencia: int, accident: AcidenteDTO):
    try:
        a = update_accident(id_ocorrencia, accident)
        if a:
            return a
        raise HTTPException(status_code=404, detail="Acidente não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{id_ocorrencia}")
def delete_accident(id_ocorrencia: int):
    try:
        ok = remove_accident(id_ocorrencia)
        if ok:
            return {"ok": ok}
        raise HTTPException(status_code=404, detail="Acidente não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
