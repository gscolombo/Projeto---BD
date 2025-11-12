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
