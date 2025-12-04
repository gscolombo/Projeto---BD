import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

from request_utils import get_companies, delete_company, update_company
from maps import create_interactive_map

st.header("Empresas Cadastradas")

companies = get_companies()

@st.dialog("Tem certeza que deseja continuar?")
def open_delete_dialog(cnpj):
    st.write(
        "Essa ação não pode ser desfeita. Registros associados também serão deletados.")

    with st.container(horizontal_alignment="right"):
        if st.button("Excluir empresa", type="primary"):
            delete_company(cnpj)
            st.rerun()


@st.dialog("Editar dados da empresa")
def open_edit_dialog(company):
    def submit_company_edit_form():
        result = update_company(company["cnpj"], {
            "cnpj": None,
            "razao_social": st.session_state.get("razao_social"),
            "nome_fantasia": st.session_state.get("nome_fantasia"),
            "lat_local": None,
            "lng_local": None
        })
        
        st.session_state["company_edit_form_result"] = result

    st.badge(f"**CNPJ**: {company['cnpj']}", color="gray")

    with st.form("company_edit_form"):
        st.text_input("Razão Social", value=company["razao_social"], key="razao_social")
        st.text_input("Nome Fantasia", value=company["nome_fantasia"], key="nome_fantasia")

        if st.form_submit_button("Salvar", on_click=submit_company_edit_form):
            st.rerun()


if "company_edit_form_result" in st.session_state:
    result = st.session_state.company_edit_form_result
    if result:
        st.toast(f"Dados do CNPJ {result["cnpj"]} alterados com sucesso.")
    del st.session_state.company_edit_form_result
    
    
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

                def emp_role(c): return "Fiscal" if c == 1 else (
                    "Motorista" if c == 2 else "Cobrador")
                if company.get('funcionarios'):
                    st.markdown("##### Funcionários")
                    employees_df = pd.DataFrame([{
                        'Nome': func['nome'],
                        'Cargo': emp_role(func['cargo']),
                        'Data Contratação': func['data_contratacao'],
                        'Data Demissão': func['data_demissao'],
                    } for func in company['funcionarios']])
                    st.dataframe(
                        employees_df, use_container_width=True, hide_index=True)

                if company.get("veiculos"):
                    st.markdown("##### Veículos")
                    vehicles_df = pd.DataFrame([{
                        'Placa': v['placa'],
                        'Quilometragem': v['km'],
                        'Ano de fabricação': v['ano_fabricacao']
                    } for v in company['veiculos']])
                    st.dataframe(
                        vehicles_df, use_container_width=True, hide_index=True)

            with col2:
                _, col_btn1, col_btn2 = st.columns([4, 1, 1])

                with col_btn1:
                    st.button("📝 Editar", key=f"edit_{company['cnpj']}",
                              type="secondary", use_container_width=True, on_click=open_edit_dialog, args=(company,))
                with col_btn2:
                    st.button("🗑️ Excluir", key=f"delete_{company['cnpj']}",
                              type="secondary", use_container_width=True, on_click=open_delete_dialog, args=(company["cnpj"],))

                st.subheader("Local da sede")
                company_map = create_interactive_map(
                    center=[company['lat_local'], company['lng_local']],
                    zoom_start=15,
                    marker_locations=[
                        (company['lat_local'], company['lng_local'])]
                )
                st_folium(company_map, use_container_width=True,
                          key=company['cnpj'], height=400)

else:
    st.info("Nenhuma empresa cadastrada.")
