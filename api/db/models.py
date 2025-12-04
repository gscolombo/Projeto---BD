from enum import Enum
from typing import List
from datetime import date, datetime
from sqlmodel import (Field, SQLModel, ForeignKeyConstraint,
                      Identity, Column, BigInteger, LargeBinary,
                      Integer, Relationship)


class Cargo(Enum):
    Fiscal = 1
    Motorista = 2
    Cobrador = 3


class StatusCNH(Enum):
    Valida = 1
    Vencida = 2
    Suspensa = 3


class Grau(Enum):
    Leve = 1
    Moderado = 2
    Grave = 3


class Local(SQLModel, table=True):
    lat: float = Field(nullable=False, primary_key=True)
    lng: float = Field(nullable=False, primary_key=True)
    nome: str | None = None
    descricao: str | None = None
    
class LocalArquivo(SQLModel, table=True):
    __tablename__ = "local_arquivo"
    
    local_lat: float = Field(nullable=False, primary_key=True)
    local_lng: float = Field(nullable=False, primary_key=True)
    nome_arquivo: str
    tipo: str
    tamanho: int
    conteudo: List[int] = Field(sa_column=Column(LargeBinary, nullable=False))
    data_upload: datetime
    
    __table_args__ = ForeignKeyConstraint(["local_lat", "local_lng"],
                                          ["local.lat", "local.lng"],
                                          ondelete="CASCADE",
                                          onupdate="CASCADE"),    


class Empresa(SQLModel, table=True):
    cnpj: str = Field(nullable=False, primary_key=True, max_length=14)
    razao_social: str
    nome_fantasia: str | None
    lat_local: float
    lng_local: float

    funcionarios: list["Funcionario"] = Relationship(back_populates="empresa")
    veiculos: list["Veiculo"] = Relationship(back_populates="empresa")
    linhas: list["Linha"] = Relationship(back_populates="empresa")

    __table_args__ = ForeignKeyConstraint(["lat_local", "lng_local"],
                                          ["local.lat", "local.lng"],
                                          ondelete="RESTRICT",
                                          onupdate="CASCADE"),


class Telefone_Funcionario(SQLModel, table=True):
    codigo_func: int = Field(
        default=None, foreign_key="funcionario.codigo", primary_key=True)
    telefone: str = Field(default=None, max_length=12, primary_key=True)

    funcionario: "Funcionario" = Relationship(back_populates="telefones")


class Funcionario(SQLModel, table=True):
    cnpj_empresa: str | None = Field(default=None,
                                     nullable=False,
                                     foreign_key='empresa.cnpj',
                                     sa_column_kwargs={"onupdate": "CASCADE"})
    codigo: int | None = Field(default=None, primary_key=True)
    nome: str
    sexo: str | None = None
    cargo: Cargo
    data_nascimento: date | None = None
    data_contratacao: date
    data_demissao: date | None = None
    telefones: list[Telefone_Funcionario] = Relationship(
        back_populates="funcionario")

    empresa: Empresa = Relationship(back_populates="funcionarios")


class Motorista(SQLModel, table=True):
    cnh: str = Field(primary_key=True, max_length=9)
    codigo_funcionario: int = Field(unique=True,
                                    foreign_key="funcionario.codigo",
                                    ondelete="CASCADE")
    status_cnh: StatusCNH
    data_validade_cnh: date


class Categoria(SQLModel, table=True):
    codigo: int = Field(primary_key=True)
    nome: str = Field(unique=True)
    descricao: str | None = None


class Modelo(SQLModel, table=True):
    codigo: int = Field(primary_key=True)
    codigo_categoria: int | None = Field(default=None,
                                         nullable=False,
                                         foreign_key="categoria.codigo")
    nome: str = Field(unique=True)


class Veiculo(SQLModel, table=True):
    placa: str = Field(primary_key=True, max_length=7)
    cnpj_empresa: str | None = Field(nullable=False,
                                     foreign_key="empresa.cnpj")
    codigo_modelo: int | None = Field(nullable=False,
                                      foreign_key="modelo.codigo")
    km: float | None = None
    ano_fabricacao: int | None = None

    empresa: Empresa = Relationship(back_populates="veiculos")
    ocorrencias: list["Ocorrencia"] = Relationship(back_populates="veiculo")


class Manutencao(SQLModel, table=True):
    id: int | None = Field(sa_column=Column(BigInteger,
                                            Identity(always=True),
                                            default=None,
                                            primary_key=True))
    placa_veiculo: str = Field(foreign_key="veiculo.placa", sa_column_kwargs={
                               "onupdate": "CASCADE"})
    data_hora: datetime


class Servico(SQLModel, table=True):
    codigo: int | None = Field(sa_column=Column(
        BigInteger, Identity(always=True), default=None, primary_key=True))
    descricao: str
    valor: float


class Manutencao_Servico(SQLModel, table=True):
    id_manutencao: int | None = Field(default=None,
                                      foreign_key="manutencao.id",
                                      primary_key=True)
    codigo_servico: int | None = Field(default=None,
                                       foreign_key="servico.codigo",
                                       primary_key=True)


class Ocorrencia(SQLModel, table=True):
    id: int | None = Field(sa_column=Column(Integer,
                                            Identity(always=True),
                                            primary_key=True,
                                            default=None))
    placa_veiculo: str = Field(foreign_key="veiculo.placa")
    data_hora: datetime
    lat_local: float
    lng_local: float

    veiculo: Veiculo = Relationship(back_populates="ocorrencias")

    __table_args__ = ForeignKeyConstraint(["lat_local", "lng_local"],
                                          ["local.lat", "local.lng"]),


class Acidente(SQLModel, table=True):
    id_ocorrencia: int | None = Field(foreign_key="ocorrencia.id",
                                      primary_key=True)
    descricao: str | None = None
    gravidade: Grau
    numero_feridos: int | None = None
    numero_mortos: int | None = None


class Avaria(SQLModel, table=True):
    id_ocorrencia: int | None = Field(foreign_key="ocorrencia.id",
                                      primary_key=True)
    descricao: str | None = None
    nivel_dano: Grau
    total: bool = False


class Linha(SQLModel, table=True):
    cnpj_empresa: str = Field(foreign_key="empresa.cnpj")
    codigo: str = Field(primary_key=True, max_length=5)

    empresa: Empresa = Relationship(back_populates="linhas")


class Itinerario(SQLModel, table=True):
    codigo_linha: str = Field(foreign_key="linha.codigo",
                              ondelete="CASCADE",
                              sa_column_kwargs={"onupdate": "CASCADE"},
                              primary_key=True)
    lat_local: float = Field(primary_key=True)
    lng_local: float = Field(primary_key=True)
    numero: int = Field(primary_key=True)

    __table_args__ = ForeignKeyConstraint(["lat_local", "lng_local"],
                                          ["local.lat", "local.lng"],
                                          onupdate="CASCADE"),


class Viagem(SQLModel, table=True):
    codigo_linha: str = Field(primary_key=True, foreign_key="linha.codigo")
    codigo_cobrador: int = Field(primary_key=True,
                                 foreign_key="funcionario.codigo")
    codigo_motorista: int = Field(primary_key=True,
                                  foreign_key="funcionario.codigo")
    placa_veiculo: str = Field(primary_key=True, foreign_key="veiculo.placa")
    data: date = Field(primary_key=True)
    hora_partida: datetime = Field(primary_key=True)
    hora_chegada: datetime | None = None
