import streamlit as st
import folium
from streamlit_folium import st_folium

from maps import create_interactive_map
from request_utils import create_company, create_location, get_locations


if "selected_location" not in st.session_state:
    st.session_state.selected_location = None

if "new_location" not in st.session_state:
    st.session_state.new_location = False

if "disable_local" not in st.session_state:
    st.session_state.disable_local = False;


@st.cache_data
def _get_locations():
    return get_locations()


def save_company():
    if not st.session_state.cnpj or len(st.session_state.cnpj) != 14:
        st.error("CNPJ deve ter 14 dígitos")
    elif not st.session_state.razao_social:
        st.error("Razão Social é obrigatória")
    elif not st.session_state.selected_location:
        st.error("Selecione uma localização no mapa")
    else:
        lat, lng = st.session_state.selected_location

        company_data = {
            "cnpj": st.session_state.cnpj,
            "razao_social": st.session_state.razao_social,
            "nome_fantasia": st.session_state.nome_fantasia,
            "lat_local": lat,
            "lng_local": lng
        }

        if st.session_state.new_location:

            location_data = {
                "lat": lat,
                "lng": lng,
                "nome": st.session_state.local_nome,
                "descricao": st.session_state.local_descricao
            }

            create_location(location_data)

        result = create_company(company_data)
        if result:
            st.success(
                f"Empresa {st.session_state.razao_social} cadastrada com sucesso!")
            st.session_state.selected_location = None
            st.cache_data.clear()


st.subheader("Cadastrar Nova Empresa")
col1, col2 = st.columns(2, vertical_alignment="center")

with col2:
    st.subheader("Local da sede")
    st.info("💡 **Clique no mapa abaixo para selecionar a localização**")

    # Get stored locations
    locations = _get_locations()

    # Create map
    m = create_interactive_map(zoom_start=10, marker_locations=[
                               (loc["lat"], loc["lng"]) for loc in locations], clickable=True)

    # Display map and get click events
    map_data = st_folium(
        m, use_container_width=True, height=400, returned_objects=["last_clicked", "last_object_clicked"])

    selected_location = selected_marker = None
    # Store clicked location
    if (map_data and
            (map_data.get("last_clicked") or map_data.get("last_object_clicked"))):
        if map_data.get("last_clicked"):
            selected_location = [
                map_data["last_clicked"]["lat"],
                map_data["last_clicked"]["lng"]
            ]
        if map_data.get("last_object_clicked"):
            selected_marker = [
                map_data["last_object_clicked"]["lat"],
                map_data["last_object_clicked"]["lng"]
            ]
        if selected_location and selected_location != st.session_state.selected_location:
            st.session_state.disable_local = False
            st.session_state.local_nome = ""
            st.session_state.local_descricao = ""
            st.session_state.selected_location = selected_location
            st.session_state.new_location = True
            st.info(
                f"Novo local selecionado: {st.session_state.selected_location[0]:.4f}, {st.session_state.selected_location[1]:.4f}")
        elif selected_marker and selected_marker != st.session_state.selected_location:
            st.session_state.selected_location = selected_marker
            st.session_state.new_location = False

            for loc in locations:
                if ((abs(selected_marker[0] - loc["lat"]) < 0.0005) and
                        (abs(selected_marker[1] - loc["lng"]) < 0.0005)):
                    st.session_state.local_nome = loc["nome"]
                    st.session_state.local_descricao = loc["descricao"]
                    st.session_state.disable_local = True
                    break

with col1:
    with st.form("new_company_form", clear_on_submit=True, height="stretch"):
        st.text_input("CNPJ (14 dígitos)", max_chars=14, key="cnpj")
        st.text_input("Razão Social", key="razao_social")
        st.text_input("Nome Fantasia", key="nome_fantasia")
        st.text_input("Nome do Local (opcional)", key="local_nome", disabled=st.session_state.disable_local)
        st.text_area("Descrição do Local (opcional)", key="local_descricao", disabled=st.session_state.disable_local)

        st.form_submit_button("Cadastrar Empresa", on_click=save_company)
