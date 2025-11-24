from fastapi import APIRouter, HTTPException

from repositories.damage import *
from repositories.dto import AvariaDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/damage", tags=["Avaria"])


@router.get("")
def get_damages():
    return list_damages()


@router.get("/{id_ocorrencia}")
def get_damage_by_id(id_ocorrencia: int):
    a = find_damage_by_id(id_ocorrencia)
    if a:
        return a
    raise HTTPException(status_code=404, detail="Avaria não encontrada.")


@router.post("", status_code=201)
def post_damage(damage: Avaria):
    try:
        id = create_damage(damage)
        return {"id_ocorrencia": id}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{id_ocorrencia}")
def put_damage(id_ocorrencia: int, damage: AvariaDTO):
    try:
        a = update_damage(id_ocorrencia, damage)
        if a:
            return a
        raise HTTPException(status_code=404, detail="Avaria não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{id_ocorrencia}")
def delete_damage(id_ocorrencia: int):
    try:
        ok = remove_damage(id_ocorrencia)
        if ok:
            return {"ok": ok}
        raise HTTPException(status_code=404, detail="Avaria não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
