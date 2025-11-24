from fastapi import APIRouter, HTTPException

from repositories.dto import LocalDTO
from repositories.local import *
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/local", tags=["Local"])


@router.get("")
def get_all_locals():
    return find_all_locals()


@router.get("/searchby")
def get_locals(lat: str | None = None, lng: str | None = None, nome: str | None = None, descricao: str | None = None):
    return find_locals_by(lat, lng, nome, descricao)


@router.post("")
def post_local(local: Local):
    try:
        lat, lng = create_local(local)
        return {"lat": lat, "lng": lng}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("")
def put_local(lat: str, lng: str, local: LocalDTO):
    try:
        l = update_local(lat, lng, local)
        if not l:
            raise HTTPException(
                status_code=404, detail="Local não encontrado.")
        return l
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("")
def put_local(lat: str, lng: str):
    try:
        if not remove_local(lat, lng):
            raise HTTPException(
                status_code=404, detail="Local não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
