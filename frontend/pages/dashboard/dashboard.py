import streamlit as st

from pages.dashboard.employee_stats import show_employee_stats
from request_utils import get_companies

st.title("🏢 Sistema de gestão da frota de ônibus do Distrito Federal")
st.header("📊 Dashboard")

# Get companies data
companies = get_companies()

if companies:
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Empresas", len(companies))
    
    with col2:
        total_employees = sum(len(company.get('funcionarios', [])) for company in companies)
        st.metric("Total de Funcionários", total_employees)
    
    with col3:
        total_vehicles = sum(len(company.get('veiculos', [])) for company in companies)
        st.metric("Total de Veículos", total_vehicles)
    
    with col4:
        total_lines = sum(len(company.get('linhas', [])) for company in companies)
        st.metric("Total de Linhas", total_lines)
    
    show_employee_stats()
else:
    st.info("Nenhuma empresa cadastrada.")