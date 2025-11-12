from fastapi import APIRouter, HTTPException

from repositories.company import *

router = APIRouter(prefix="/empresa", tags=["Empresa"])

@router.get("/")
def get_company():
    return get_company_data()

@router.get("/searchby")
def get_company(cnpj: str = None, company_name: str = None, trade_name: str = None):
    c = find_company(cnpj, company_name, trade_name)

    if (c): return c
    raise HTTPException(status_code=404, detail="Empresa não encontrada")
