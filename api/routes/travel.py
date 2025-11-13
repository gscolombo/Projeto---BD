from fastapi import APIRouter, HTTPException

from repositories.travel import *
from repositories.dto import ViagemDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/viagem", tags=["Viagem"])


@router.get("")
def get_travels():
    return list_travels()


@router.get("/{codigo_linha}/{codigo_cobrador}/{codigo_motorista}/{placa_veiculo}/{data}/{hora_partida}")
def get_travel(codigo_linha: str, codigo_cobrador: int, codigo_motorista: int, placa_veiculo: str, data: str, hora_partida: str):
    v = find_travel(codigo_linha, codigo_cobrador,
                    codigo_motorista, placa_veiculo, data, hora_partida)
    if v:
        return v
    raise HTTPException(status_code=404, detail="Viagem não encontrada.")


@router.post("", status_code=201)
def post_travel(travel: Viagem):
    try:
        codigo_linha, codigo_cobrador, codigo_motorista, placa_veiculo, data, hora_partida = create_travel(
            travel)
        return {
            "codigo_linha": codigo_linha,
            "codigo_cobrador": codigo_cobrador,
            "codigo_motorista": codigo_motorista,
            "placa_veiculo": placa_veiculo,
            "data": data,
            "hora_partida": hora_partida
        }
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{codigo_linha}/{codigo_cobrador}/{codigo_motorista}/{placa_veiculo}/{data}/{hora_partida}")
def put_travel(codigo_linha: str, codigo_cobrador: int, codigo_motorista: int, placa_veiculo: str, data: str, hora_partida: str, travel: ViagemDTO):
    try:
        v = update_travel(codigo_linha, codigo_cobrador,
                          codigo_motorista, placa_veiculo, data, hora_partida, travel)
        if v:
            return v
        raise HTTPException(status_code=404, detail="Viagem não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{codigo_linha}/{codigo_cobrador}/{codigo_motorista}/{placa_veiculo}/{data}/{hora_partida}")
def delete_travel(codigo_linha: str, codigo_cobrador: int, codigo_motorista: int, placa_veiculo: str, data: str, hora_partida: str):
    try:
        ok = remove_travel(codigo_linha, codigo_cobrador,
                           codigo_motorista, placa_veiculo, data, hora_partida)
        if ok:
            return {"ok": ok}
        raise HTTPException(status_code=404, detail="Viagem não encontrada.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
