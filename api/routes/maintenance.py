from fastapi import APIRouter, HTTPException

from repositories.maintenance import *
from repositories.dto import ManutencaoDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/manutencao", tags=["Manutenção"])


@router.get("")
def get_maintenances():
    return list_maintenances()


@router.get("/{id}")
def get_maintenance_by_id(id: int):
    m = find_maintenance_by_id(id)
    if m:
        return m
    raise HTTPException(status_code=404, detail="Manutenção não encontrada.")


@router.post("", status_code=201)
def post_maintenance(maintenance: Manutencao):
    try:
        id = create_maintenance(maintenance)
        return {"id": id}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{id}")
def put_maintenance(id: int, maintenance: ManutencaoDTO):
    try:
        m = update_maintenance(id, maintenance)
        if m:
            return m
        raise HTTPException(
            status_code=404, detail="Manutenção não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{id}")
def delete_maintenance(id: int):
    try:
        ok = remove_maintenance(id)
        if ok:
            return {"ok": ok}
        raise HTTPException(
            status_code=404, detail="Manutenção não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
