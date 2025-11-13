from fastapi import APIRouter, HTTPException

from repositories.employee import *
from repositories.dto import FuncionarioDTO

router = APIRouter(prefix="/funcionario", tags=["Funcionário"])


@router.get("")
def get_employees():
    return list_employees()


@router.get("/like")
def get_employee_by_name(nome: str):
    f = find_employee_by_name(nome)
    if f:
        return f
    raise HTTPException(status_code=404, detail="Funcionário não encontrado.")


@router.get("/{codigo}")
def get_employee_by_id(codigo: int):
    f = find_employee_by_id(codigo)
    if f:
        return f
    raise HTTPException(status_code=404, detail="Funcionário não encontrado.")


@router.post("", status_code=201)
def post_employee(employee: Funcionario):
    id = create_employee(employee)
    return {"id": id}


@router.put("/{codigo}")
def put_employee(codigo: int, employee: FuncionarioDTO):
    w = update_employee(codigo, employee)
    if w:
        return w
    raise HTTPException(status_code=404, detail="Funcionário não encontrado.")


@router.delete("/{codigo}")
def delete_employee(codigo: int):
    ok = remove_employee(codigo)
    if ok:
        return {"ok": ok}
    raise HTTPException(status_code=404, detail="Funcionário não encontrado.")
