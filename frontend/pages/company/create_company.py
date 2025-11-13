import streamlit as st
from streamlit_folium import st_folium

from maps import create_interactive_map
from request_utils import create_company, create_location

if "selected_location" not in st.session_state:
    st.session_state.selected_location = None

def save_company():
    if not st.session_state.cnpj or len(st.session_state.cnpj) != 14:
        st.error("CNPJ deve ter 14 dígitos")
    elif not st.session_state.razao_social:
        st.error("Razão Social é obrigatória")
    elif not st.session_state.selected_location:
        st.error("Selecione uma localização no mapa")
    else:
        lat, lng = st.session_state.selected_location

        location_data = {
            "lat": lat,
            "lng": lng,
            "nome": st.session_state.local_nome,
            "descricao": st.session_state.local_descricao
        }

        location_result = create_location(location_data)
        if location_result is not None:
            company_data = {
                "cnpj": st.session_state.cnpj,
                "razao_social": st.session_state.razao_social,
                "nome_fantasia": st.session_state.nome_fantasia,
                "lat_local": lat,
                "lng_local": lng
            }

            result = create_company(company_data)
            if result:
                st.success(
                    f"Empresa {st.session_state.razao_social} cadastrada com sucesso!")
                st.session_state.selected_location = None


st.subheader("Cadastrar Nova Empresa")
with st.form("new_company_form", clear_on_submit=True, height="stretch"):
    col1, col2 = st.columns(2, vertical_alignment="center")

    with col1:
        st.text_input("CNPJ (14 dígitos)", max_chars=14, key="cnpj")
        st.text_input("Razão Social", key="razao_social")
        st.text_input("Nome Fantasia", key="nome_fantasia")
        st.text_input("Nome do Local (opcional)", key="local_nome")
        st.text_area("Descrição do Local (opcional)",
                     key="local_descricao")

    with col2:
        st.subheader("Local da sede")
        st.info("💡 **Clique no mapa abaixo para selecionar a localização**")

        # Create map
        m = create_interactive_map(zoom_start=10)

        # Display map and get click events
        map_data = st_folium(
            m, use_container_width=True, height=320, key="company_local")

        # Store clicked location
        if map_data and map_data.get("last_clicked"):
            st.session_state.selected_location = [
                map_data["last_clicked"]["lat"],
                map_data["last_clicked"]["lng"]
            ]

    st.form_submit_button("Cadastrar Empresa", on_click=save_company)
