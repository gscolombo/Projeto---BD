from fastapi import APIRouter, HTTPException

from repositories.maintenance_service import *
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/manutencao-servico", tags=["Manutenção-Serviço"])


@router.get("")
def get_maintenance_services():
    return list_maintenance_services()


@router.get("/manutencao/{id_manutencao}")
def get_services_by_maintenance(id_manutencao: int):
    services = find_services_by_maintenance(id_manutencao)
    if services:
        return services
    raise HTTPException(
        status_code=404, detail="Serviços não encontrados para a manutenção.")


@router.post("", status_code=201)
def post_manutencao_servico(manutencao_servico: Manutencao_Servico):
    try:
        id_manutencao, codigo_servico = create_maintenance_service(
            manutencao_servico)
        return {"id_manutencao": id_manutencao, "codigo_servico": codigo_servico}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{id_manutencao}/{codigo_servico}")
def delete_manutencao_servico(id_manutencao: int, codigo_servico: int):
    try:
        ok = remove_maintenance_service(id_manutencao, codigo_servico)
        if ok:
            return {"ok": ok}
        raise HTTPException(
            status_code=404, detail="Relação manutenção-serviço não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
