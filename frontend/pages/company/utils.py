import streamlit as st

from request_utils import call_save_new_company

def save_company():
    if not st.session_state.cnpj or len(st.session_state.cnpj) != 14:
        st.error("CNPJ deve ter 14 dígitos")
        return
    elif not st.session_state.razao_social:
        st.error("Razão Social é obrigatória")
        return
    elif not st.session_state.selected_location:
        st.error("Selecione uma localização no mapa")
        return

    lat, lng = st.session_state.selected_location

    new_company_data = {
        "cnpj": st.session_state.cnpj,
        "razao_social": st.session_state.razao_social,
        "nome_fantasia": st.session_state.nome_fantasia,
        "lat_local": lat,
        "lng_local": lng,
        "local_nome": st.session_state.local_nome,
        "local_descricao": st.session_state.local_descricao,
        "employees": st.session_state.employees,
        "vehicles": st.session_state.vehicles
    }
    
    print(new_company_data)
    
    result = call_save_new_company(new_company_data)

    if (result):
        # Success message
        st.success(f"""
        CNPJ {result["cnpj"]} cadastrado com sucesso!
        - Funcionários cadastrados: {result["funcionarios_criados"]}
        - Veículos cadastrados: {result["veiculos_criados"]}
        """)

        # Reset form
        st.session_state.selected_location = None
        st.session_state.employees = []
        st.session_state.vehicles = []
        st.cache_data.clear()
