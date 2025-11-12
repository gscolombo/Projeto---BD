from fastapi import APIRouter, HTTPException

from repositories.worker import *

router = APIRouter(prefix="/funcionarios", tags=["empresa"])


@router.get("/")
def get_workers():
    return list_workers()


@router.get("/like")
def get_worker_by_name(nome: str):
    f = find_worker_by_name(nome)
    if f:
        return f
    raise HTTPException(status_code=404, detail="Funcionário não encontrado.")


@router.get("/{codigo}")
def get_worker_by_id(codigo: int):
    f = find_worker_by_id(codigo)
    if f:
        return f
    raise HTTPException(status_code=404, detail="Funcionário não encontrado.")
