from fastapi import APIRouter, HTTPException

from repositories.itinerary import *
from repositories.dto import ItinerarioDTO
from routes.exception import CustomHTTPException

router = APIRouter(prefix="/itinerario", tags=["Itinerário"])


@router.get("")
def get_itinerarios():
    return list_itineraries()


@router.get("/linha/{codigo_linha}")
def get_itineraries_by_line(codigo_linha: str):
    itinerarios = find_itinerary_by_line(codigo_linha)
    if itinerarios:
        return itinerarios
    raise HTTPException(
        status_code=404, detail="Itinerário não encontrado para a linha.")


@router.post("", status_code=201)
def post_itinerary(itinerario: Itinerario):
    try:
        codigo_linha, lat_local, lng_local, numero = create_itinerary(
            itinerario)
        return {"codigo_linha": codigo_linha, "lat_local": lat_local, "lng_local": lng_local, "numero": numero}
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.put("/{codigo_linha}/{lat_local}/{lng_local}/{numero}")
def put_itinerary(codigo_linha: str, lat_local: float, lng_local: float, numero: int, itinerario: ItinerarioDTO):
    try:
        i = update_itinerary(codigo_linha, lat_local,
                              lng_local, numero, itinerario)
        if i:
            return i
        raise HTTPException(
            status_code=404, detail="Itinerário não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))


@router.delete("/{codigo_linha}/{lat_local}/{lng_local}/{numero}")
def delete_itinerary(codigo_linha: str, lat_local: float, lng_local: float, numero: int):
    try:
        ok = remove_itinerary(codigo_linha, lat_local, lng_local, numero)
        if ok:
            return {"ok": ok}
        raise HTTPException(
            status_code=404, detail="Itinerário não encontrado.")
    except Exception as e:
        raise CustomHTTPException(
            400, "Erro durante processamento de consulta", str(e))
