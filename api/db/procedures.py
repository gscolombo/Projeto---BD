from typing import List, Optional
from pydantic import BaseModel

class MotoristaData(BaseModel):
    cnh: str
    status_cnh: str
    data_validade_cnh: str

class EmployeeData(BaseModel):
    nome: str
    sexo: Optional[str] = None
    cargo: str
    data_nascimento: Optional[str] = None
    data_contratacao: str
    telefones: List[str] = []
    motorista_data: Optional[MotoristaData] = None
    
class VehicleData(BaseModel):
    placa: str
    codigo_modelo: int
    km: float = 0.
    ano_fabricacao: Optional[int] = None

class NewCompanyData(BaseModel):
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = None
    lat_local: float
    lng_local: float
    local_nome: Optional[str] = None
    local_descricao: Optional[str] = None
    employees: List[EmployeeData] = []
    vehicles: List[VehicleData] = []
    

