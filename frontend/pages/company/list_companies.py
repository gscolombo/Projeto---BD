import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

from request_utils import get_companies
from maps import create_interactive_map

st.header("Empresas Cadastradas")

companies = get_companies()

if companies:
    # Display companies in an expandable format
    for company in companies:
        with st.expander(f"{company['razao_social']}"):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f'''
                    ### {company.get('nome_fantasia', 'Não informado')}
                ''')
                st.badge(f"**CNPJ**: {company['cnpj']}", color="gray")

                emp_role = lambda c: "Fiscal" if c == 1 else ("Motorista" if c == 2 else "Cobrador")
                if company.get('funcionarios'):
                    st.markdown("##### Funcionários")
                    employees_df = pd.DataFrame([{
                        'Nome': func['nome'],
                        'Cargo': emp_role(func['cargo']),
                        'Data Contratação': func['data_contratacao']
                    } for func in company['funcionarios']])
                    st.dataframe(employees_df, use_container_width=True, hide_index=True)

                if company.get("veiculos"):
                    st.markdown("##### Veículos")
                    vehicles_df = pd.DataFrame([{
                        'Placa': v['placa'],
                        'Quilometragem': v['km'],
                        'Ano de fabricação': v['ano_fabricacao']
                    } for v in company['veiculos']])
                    st.dataframe(vehicles_df, use_container_width=True, hide_index=True)

            with col2:
                st.subheader("Local da sede")
                company_map = create_interactive_map(
                    center=[company['lat_local'], company['lng_local']],
                    zoom_start=15,
                    marker_location=[
                        company['lat_local'], company['lng_local']]
                )
                st_folium(company_map, use_container_width=True, height=400)


else:
    st.info("Nenhuma empresa cadastrada.")
