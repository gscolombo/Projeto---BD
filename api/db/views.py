from sqlmodel import SQLModel, Field

class EmployeeOverviewByCompany(SQLModel, table=True):
    __tablename__ = "employee_overview_by_company"
    cnpj: str = Field(primary_key=True)
    razao_social: str
    nome_fantasia: str
    nome: str
    sexo: str
    cargo: str
    idade_funcionario: int
    
class VehicleOverviewByCompany(SQLModel, table=True):
    __tablename__ = "vehicle_overview_by_company"
    cnpj: str = Field(primary_key=True)
    razao_social: str
    nome_fantasia: str
    placa: str
    km: float
    ano_fabricacao: int
    modelo: str
    categoria: str
    
class EmployeeStats(SQLModel, table=True):
    __tablename__ = "employee_stats"
    cnpj: str = Field(primary_key=True)
    nome_fantasia: str
    quant_funcionarios: int
    proporcao_homens: float
    proporcao_motorista: float
    proporcao_cobrador: float
    proporcao_fiscal: float
    idade_media: float