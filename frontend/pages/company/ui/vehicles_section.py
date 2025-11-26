import streamlit as st

from request_utils import get_models


def add_vehicle():
    """Add a new empty vehicle to the list"""
    st.session_state.vehicles.append({
        "placa": "",
        "codigo_modelo": "",
        "km": 0.0,
        "ano_fabricacao": None
    })


def remove_vehicle(index):
    """Remove vehicle from list"""
    st.session_state.vehicles.pop(index)


@st.cache_data
def get_vehicle_models():
    return get_models()


def vehicles_section():
    models = get_vehicle_models()

    # Vehicles Section
    st.subheader("Veículos")

    # Add vehicle button
    st.button("➕ Adicionar Veículo", on_click=add_vehicle)

    if not st.session_state.vehicles:
        st.info("Nenhum veículo adicionado")

    for i, vehicle in enumerate(st.session_state.vehicles):
        with st.expander(f"Veículo {i+1}", expanded=True):
            col_veh1, col_veh2 = st.columns(2)

            with col_veh1:
                vehicle["placa"] = st.text_input("Placa",
                                                 value=vehicle["placa"],
                                                 max_chars=7,
                                                 key=f"placa_{i}")
                vehicle["codigo_modelo"] = st.selectbox("Modelo", [m["codigo"] for m in models],
                                                        index=None,
                                                        placeholder="Selecione um modelo",
                                                        format_func=lambda i: [m["nome"] for m in models if m["codigo"] == i][0],
                                                        key=f"modelo_{i}")

            with col_veh2:
                vehicle["km"] = st.number_input("Quilometragem",
                                                value=float(vehicle["km"]),
                                                min_value=0.0,
                                                key=f"km_{i}")
                vehicle["ano_fabricacao"] = st.number_input("Ano de Fabricação",
                                                            value=vehicle["ano_fabricacao"] or 2024,
                                                            min_value=1900,
                                                            max_value=2030,
                                                            key=f"ano_{i}")

            st.button("❌ Remover Veículo", key=f"remove_veh_{i}",
                      on_click=remove_vehicle, args=(i,))
