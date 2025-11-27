import streamlit as st
from datetime import datetime, timedelta


def add_employee():
    """Add a new empty employee to the list"""
    st.session_state.employees.append({
        "nome": "",
        "sexo": "",
        "cargo": None,
        "data_nascimento": None,
        "data_contratacao": None,
        "telefones": [],
        "motorista_data": None
    })


def remove_employee(index):
    """Remove employee from list"""
    st.session_state.employees.pop(index)


def add_employee_phone(emp_index):
    """Add another phone number for an employee"""
    st.session_state.employees[emp_index]["telefones"].append("")


def remove_employee_phone(emp_index, phone_index):
    """Remove phone number from employee"""
    if len(st.session_state.employees[emp_index]["telefones"]) > 1:
        st.session_state.employees[emp_index]["telefones"].pop(phone_index)


def employees_section():
    # Employees Section
    st.subheader("Funcionários")

    # Add employee button
    st.button("➕ Adicionar Funcionário", on_click=add_employee)

    if not st.session_state.employees:
        st.info("Nenhum funcionário adicionado")

    for i, emp in enumerate(st.session_state.employees):
        with st.expander(f"Funcionário {i+1}", expanded=True):
            col_emp1, col_emp2 = st.columns(2)

            with col_emp1:
                emp["nome"] = st.text_input(
                    "Nome", value=emp["nome"], key=f"emp_nome_{i}")
                emp["sexo"] = st.selectbox("Sexo", ["M", "F"],
                                           index=None if not emp["sexo"] else (
                                               0 if emp["sexo"] == "M" else 1),
                                           placeholder="Selecione uma opção",
                                           key=f"emp_sexo_{i}")
                
                role_options = ["Fiscal", "Motorista", "Cobrador"]
                emp["cargo"] = st.selectbox("Cargo",
                                            role_options,
                                            index=None if not emp["cargo"] else role_options.index(emp["cargo"]),
                                            placeholder="Selecione uma opção",
                                            key=f"emp_cargo_{i}")

            with col_emp2:

                birth_date = st.date_input("Data de Nascimento",
                                           value=emp["data_nascimento"],
                                           min_value=datetime.today() - timedelta(days=365 * 101),
                                           max_value="today",
                                           key=f"emp_nasc_{i}")
                hiring_date = st.date_input("Data de Contratação",
                                            value=emp["data_contratacao"],
                                            min_value=datetime(1950, month=1, day=1),
                                            max_value="today",
                                            key=f"emp_contratacao_{i}")

                emp["data_nascimento"] = birth_date.strftime("%Y-%m-%d") if birth_date else None
                emp["data_contratacao"] = hiring_date.strftime("%Y-%m-%d") if hiring_date else None

            # Phone numbers
            st.write("Telefones:")
            for j, phone in enumerate(emp["telefones"]):
                col_phone1, col_phone2 = st.columns(
                    [4, 1], vertical_alignment="bottom")
                with col_phone1:
                    emp["telefones"][j] = st.text_input(f"Telefone {j+1}",
                                                        value=phone,
                                                        key=f"emp_phone_{i}_{j}")
                with col_phone2:
                    st.button("❌", key=f"remove_phone_{i}_{j}",
                              on_click=remove_employee_phone,
                              args=(i, j))

            st.button("➕ Adicionar Telefone", key=f"add_phone_{i}",
                      on_click=add_employee_phone, args=(i,))

            # Motorista section
            if emp["cargo"] == "Motorista":
                st.subheader("Dados do Motorista")
                col_mot1, col_mot2 = st.columns(2)

                with col_mot1:
                    emp["motorista_data"]["cnh"] = st.text_input("CNH",
                                                                 value=emp["motorista_data"]["cnh"],
                                                                 max_chars=9,
                                                                 key=f"cnh_{i}")

                with col_mot2:
                    status_options = ["Válida", "Vencida", "Suspensa"]
                    emp["motorista_data"]["status_cnh"] = st.selectbox("Status CNH",
                                                                       status_options,
                                                                       index=None if not emp["motorista_data"]["status_cnh"]
                                                                                else status_options.index(emp["motorista_data"]["status_cnh"]),
                                                                       placeholder="Selecione uma opção",
                                                                       key=f"status_cnh_{i}")

                due_date = st.date_input("Data de Validade CNH",
                                         value=emp["motorista_data"]["data_validade_cnh"],
                                         key=f"validade_cnh_{i}")

                emp["motorista_data"]["data_validade_cnh"] = due_date.strftime("%Y-%m-%d") if due_date else None

            st.button("❌ Remover Funcionário", key=f"remove_emp_{i}",
                      on_click=remove_employee, args=(i,))
