# create_company.py
import streamlit as st

from pages.company.ui.employees_section import employees_section
from pages.company.ui.vehicles_section import vehicles_section
from pages.company.ui.location_setter import location_map
from pages.company.utils import save_company

if "employees" not in st.session_state:
    st.session_state.employees = []

if "vehicles" not in st.session_state:
    st.session_state.vehicles = []

if "selected_location" not in st.session_state:
    st.session_state.selected_location = None

if "selected_marker" not in st.session_state:
    st.session_state.selected_marker = None

if "selected_point" not in st.session_state:
    st.session_state.selected_point = None

if "new_location" not in st.session_state:
    st.session_state.new_location = False

if "disable_local" not in st.session_state:
    st.session_state.disable_local = False

# Main UI
st.subheader("Cadastrar Nova Empresa")

# Company and Location Section
col1, col2 = st.columns(2, vertical_alignment="top", border=True)

with col2:
    location_map()
with col1:
    st.subheader("Dados da Empresa")
    st.text_input("CNPJ (14 dígitos)", max_chars=14, key="cnpj")
    st.text_input("Razão Social", key="razao_social")
    st.text_input("Nome Fantasia", key="nome_fantasia")

    employees_section()
    vehicles_section()

    # Final submit button
    st.button("Enviar", on_click=save_company)
