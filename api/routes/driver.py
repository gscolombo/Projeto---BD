from fastapi import APIRouter, HTTPException

from repositories.driver import *
from repositories.dto import MotoristaDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/motorista", tags=["Motorista"])

@router.get("")
def get_drivers():
    return list_drivers()

@router.get("/{cnh}")
def get_driver_by_cnh(cnh: str):
    m = find_driver_by_cnh(cnh)
    if m:
        return m
    raise HTTPException(status_code=404, detail="Motorista não encontrado.")

@router.get("/funcionario/{codigo_funcionario}")
def get_driver_by_employee(codigo_funcionario: int):
    m = find_driver_by_employee(codigo_funcionario)
    if m:
        return m
    raise HTTPException(status_code=404, detail="Motorista não encontrado.")

@router.post("", status_code=201)
def post_driver(driver: Motorista):
    try:
        cnh = create_driver(driver)
        return {"cnh": cnh}
    except Exception as e:
        raise CustomHTTPException(400, "Erro durante processamento de consulta", str(e))

@router.put("/{cnh}")
def put_driver(cnh: str, driver: MotoristaDTO):
    try:
        m = update_driver(cnh, driver)
        if m:
            return m
        raise HTTPException(status_code=404, detail="Motorista não encontrado.")
    except Exception as e:
        raise CustomHTTPException(400, "Erro durante processamento de consulta", str(e))

@router.delete("/{cnh}")
def delete_driver(cnh: str):
    try:
        ok = remove_driver(cnh)
        if ok:
            return {"ok": ok}
        raise HTTPException(status_code=404, detail="Motorista não encontrado.")
    except Exception as e:
        raise CustomHTTPException(400, "Erro durante processamento de consulta", str(e))