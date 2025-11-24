from fastapi import APIRouter, HTTPException

from repositories.company import *
from repositories.dto import EmpresaDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/empresa", tags=["Empresa"])


@router.get("")
def get_company():
    return get_company_data()


@router.get("/searchby")
def get_company(cnpj: str = None, company_name: str = None, trade_name: str = None):
    c = find_company(cnpj, company_name, trade_name)

    if (c):
        return c
    raise HTTPException(status_code=404, detail="Empresa não encontrada")


@router.post("")
def post_company(company: Empresa):
    try:
        cnpj = create_company(company)
        return {"cnpj": cnpj}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("")
def put_company(cnpj: str, company: EmpresaDTO):
    try:
        c = update_company(cnpj, company)
        if c:
            return c
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("")
def delete_company(cnpj: str):
    try:
        if not remove_company(cnpj):
            raise HTTPException(
                status_code=404, detail="Empresa não encontrada")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
