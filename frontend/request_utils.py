import streamlit as st
import requests

API_BASE_URL = "http://localhost:8000" 

def make_request(method, endpoint, **kwargs):
    """Helper function to make API requests"""
    url = f"{API_BASE_URL}{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url, **kwargs)
        elif method == "POST":
            response = requests.post(url, **kwargs)
        elif method == "PUT":
            response = requests.put(url, **kwargs)
        elif method == "DELETE":
            response = requests.delete(url, **kwargs)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 201:
            return response.json()
        else:
            st.error(f"Erro {response.status_code}: {response.text}")
            return None
    except requests.exceptions.ConnectionError:
        st.error(
            "Não foi possível conectar ao servidor. Verifique se a API está rodando.")
        return None
    except Exception as e:
        st.error(f"Erro inesperado: {str(e)}")
        return None


def get_companies():
    """Get all companies"""
    return make_request("GET", "/empresa")


def get_company_by_cnpj(cnpj):
    """Get company by CNPJ"""
    return make_request("GET", f"/empresa/searchby?cnpj={cnpj}")


def create_company(company_data):
    """Create new company"""
    return make_request("POST", "/empresa", json=company_data)


def update_company(cnpj, company_data):
    """Update company"""
    return make_request("PUT", f"/empresa?cnpj={cnpj}", json=company_data)


def delete_company(cnpj):
    """Delete company"""
    return make_request("DELETE", f"/empresa?cnpj={cnpj}")


def get_locations():
    """Get all locations"""
    return make_request("GET", "/local")

def create_location(location_data):
    """Create new location"""
    return make_request("POST", "/local", json=location_data)

def upload_location_image(location_image_data):
    """Upload location image"""
    return make_request("POST", "/local/imagem", json=location_image_data)

def create_employee(employee_data):
    """Create new employee"""
    return make_request("POST", "/funcionario", json=employee_data)

def create_vehicle(vehicle_data):
    """Create new vehicle"""
    return make_request("POST", "/veiculo", json=vehicle_data)

def get_models():
    """Get vehicle models"""
    return make_request("GET", "/modelo")

def create_driver(motorista_data):
    """Create new driver"""
    return make_request("POST", "/motorista", json=motorista_data)

def call_save_new_company(company_data):
    """Call "save_new_company" procedure"""
    return make_request("POST", "/empresa/extended", json=company_data)

def delete_company(cnpj):
    return make_request("DELETE", f"/empresa?cnpj={cnpj}")

def get_employee_stats():
    return make_request("GET", "/funcionario/view/employee_stats")