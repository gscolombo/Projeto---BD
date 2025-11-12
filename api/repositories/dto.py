from sqlmodel import SQLModel
from datetime import date

from db.models import Cargo


class FuncionarioDTO(SQLModel):
    nome: str | None = None
    sexo: str | None = None
    cargo: Cargo | None = None
    data_nascimento: date | None = None
    data_contratacao: date | None = None
    data_demissao: date | None = None


class EmpresaDTO(SQLModel):
    cnpj: str | None = None
    razao_social: str | None = None
    nome_fantasia: str | None = None
    lat_local: float | None = None
    lng_local: float | None = None