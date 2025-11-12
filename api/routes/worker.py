from fastapi import APIRouter, HTTPException

from repositories.worker import *
from repositories.dto import FuncionarioDTO

router = APIRouter(prefix="/funcionarios", tags=["Funcionário"])


@router.get("")
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


@router.post("", status_code=201)
def post_worker(worker: Funcionario):
    id = create_worker(worker)
    return {"id": id}


@router.put("/{codigo}")
def put_worker(codigo: int, worker: FuncionarioDTO):
    w = update_worker(codigo, worker)
    if w:
        return w
    raise HTTPException(status_code=404, detail="Funcionário não encontrado.")


@router.delete("/{codigo}")
def delete_worker(codigo: int):
    ok = remove_worker(codigo)
    if ok:
        return {"ok": ok}
    raise HTTPException(status_code=404, detail="Funcionário não encontrado.")
