from fastapi import APIRouter, HTTPException

from repositories.vehicle import *
from repositories.dto import VeiculoDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/veiculo", tags=["Veículo"])


@router.get("")
def get_vehicles():
    return list_vehicles()


@router.get("/{placa}")
def get_vehicle_by_placa(placa: str):
    v = find_vehicle_by_placa(placa)
    if v:
        return v
    raise HTTPException(status_code=404, detail="Veículo não encontrado.")


@router.get("/empresa/{cnpj_empresa}")
def get_vehicles_by_empresa(cnpj: str):
    vehicles = find_vehicles_by_company(cnpj)
    if vehicles:
        return vehicles
    raise HTTPException(
        status_code=404, detail="Veículos não encontrados para a empresa.")


@router.post("", status_code=201)
def post_vehicle(vehicle: Veiculo):
    try:
        placa = create_vehicle(vehicle)
        return {"placa": placa}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{placa}")
def put_vehicle(placa: str, vehicle: VeiculoDTO):
    try:
        v = update_vehicle(placa, vehicle)
        if v:
            return v
        raise HTTPException(status_code=404, detail="Veículo não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{placa}")
def delete_vehicle(placa: str):
    try:
        ok = remove_vehicle(placa)
        if ok:
            return {"ok": ok}
        raise HTTPException(status_code=404, detail="Veículo não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
