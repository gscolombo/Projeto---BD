import streamlit as st

from request_utils import create_company, create_location, create_employee, create_vehicle, create_driver

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

    # Create location if new
    if st.session_state.new_location:
        location_data = {
            "lat": lat,
            "lng": lng,
            "nome": st.session_state.local_nome,
            "descricao": st.session_state.local_descricao
        }
        create_location(location_data)

    # Create company
    company_data = {
        "cnpj": st.session_state.cnpj,
        "razao_social": st.session_state.razao_social,
        "nome_fantasia": st.session_state.nome_fantasia,
        "lat_local": lat,
        "lng_local": lng
    }

    company_result = create_company(company_data)
    if not company_result:
        st.error("Erro ao cadastrar empresa")
        return

    # Create employees
    employees_created = []
    for emp in st.session_state.employees:
        if emp["nome"] and emp["data_contratacao"]:
            employee_data = {
                "cnpj_empresa": st.session_state.cnpj,
                "nome": emp["nome"],
                "sexo": emp["sexo"],
                "cargo": emp["cargo"],
                "data_nascimento": emp["data_nascimento"].isoformat() if emp["data_nascimento"] else None,
                "data_contratacao": emp["data_contratacao"].isoformat(),
                "telefones": [phone for phone in emp["telefones"] if phone]
            }

            employee_result = create_employee(employee_data)
            if employee_result:
                employees_created.append(employee_result)

                # Create motorista if applicable
                if emp["is_motorista"] and emp["motorista_data"]["cnh"] and emp["motorista_data"]["data_validade_cnh"]:
                    motorista_data = {
                        "cnh": emp["motorista_data"]["cnh"],
                        "codigo_funcionario": employee_result.get("codigo"),
                        "status_cnh": emp["motorista_data"]["status_cnh"],
                        "data_validade_cnh": emp["motorista_data"]["data_validade_cnh"].isoformat()
                    }
                    # You would need to add create_motorista function in request_utils.py
                    create_driver(motorista_data)

    # Create vehicles
    vehicles_created = []
    for vehicle in st.session_state.vehicles:
        if vehicle["placa"] and vehicle["codigo_modelo"]:
            vehicle_data = {
                "placa": vehicle["placa"],
                "cnpj_empresa": st.session_state.cnpj,
                "codigo_modelo": vehicle["codigo_modelo"],
                "km": vehicle["km"],
                "ano_fabricacao": vehicle["ano_fabricacao"]
            }

            vehicle_result = create_vehicle(vehicle_data)
            if vehicle_result:
                vehicles_created.append(vehicle_result)

    # Success message
    st.success(f"""
    Empresa {st.session_state.razao_social} cadastrada com sucesso!
    - Funcionários cadastrados: {len(employees_created)}
    - Veículos cadastrados: {len(vehicles_created)}
    """)

    # Reset form
    st.session_state.selected_location = None
    st.session_state.employees = []
    st.session_state.vehicles = []
    st.cache_data.clear()
