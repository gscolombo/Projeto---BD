from fastapi import APIRouter, HTTPException

from repositories.company import *
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
