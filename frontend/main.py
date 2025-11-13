import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Sistema de Gestão de Empresas",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize map center (Brazil coordinates)
if 'map_center' not in st.session_state:
    st.session_state.map_center = [-15.77972, -47.92972]  # Brasília


pages = {
    "": [st.Page("pages/dashboard.py", title="📊 Dashboard", default=True)],
    "🏢 Empresas": [
        st.Page("pages/company/list_companies.py", title="Empresas cadastradas"),
        st.Page("pages/company/create_company.py", title="Cadastrar nova empresa")
    ]
}

pg = st.navigation(pages, position="top")
pg.run()

