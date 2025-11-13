from sqlmodel import SQLModel
from datetime import date, datetime

from db.models import StatusCNH, Grau, Cargo


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


class LocalDTO(SQLModel):
    lat: float | None = None
    lng: float | None = None
    nome: str | None = None
    descricao: str | None = None


class MotoristaDTO(SQLModel):
    status_cnh: StatusCNH | None = None
    data_validade_cnh: date | None = None


class VeiculoDTO(SQLModel):
    cnpj_empresa: str | None = None
    codigo_modelo: int | None = None
    km: float | None = None
    ano_fabricacao: int | None = None


class ModeloDTO(SQLModel):
    codigo_categoria: int | None = None
    nome: str | None = None


class CategoriaDTO(SQLModel):
    nome: str | None = None
    descricao: str | None = None


class OcorrenciaDTO(SQLModel):
    placa_veiculo: str | None = None
    data_hora: datetime | None = None
    lat_local: float | None = None
    lng_local: float | None = None


class AcidenteDTO(SQLModel):
    descricao: str | None = None
    gravidade: Grau | None = None
    numero_feridos: int | None = None
    numero_mortos: int | None = None


class AvariaDTO(SQLModel):
    descricao: str | None = None
    nivel_dano: Grau | None = None
    total: bool | None = None


class ManutencaoDTO(SQLModel):
    placa_veiculo: str | None = None
    data_hora: datetime | None = None


class ServicoDTO(SQLModel):
    descricao: str | None = None
    valor: float | None = None


class LinhaDTO(SQLModel):
    cnpj_empresa: str | None = None
    codigo: str | None = None


class ItinerarioDTO(SQLModel):
    codigo_linha: str | None = None
    lat_local: float | None = None
    lng_local: float | None = None
    numero: int | None = None


class ViagemDTO(SQLModel):
    codigo_linha: str | None = None
    codigo_cobrador: int | None = None
    codigo_motorista: int | None = None
    placa_veiculo: str | None = None
    data: date | None = None
    hora_partida: datetime | None = None
    hora_chegada: datetime | None = None
