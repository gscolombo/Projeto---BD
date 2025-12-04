import streamlit as st
from request_utils import upload_location_image, get_locations
from datetime import datetime
from base64 import b64encode

if "upload_image_result" not in st.session_state:
    st.session_state.upload_image_result = None

@st.cache_data
def _get_locations():
    return get_locations()
    

st.title("Upload de imagem para Local")

if (result := st.session_state.upload_image_result):
    st.success(f"Arquivo {result["nome_arquivo"]} salvo com sucesso!")
    st.session_state.upload_image_result = None
    st.session_state.location_selectbox = None
    

locations = _get_locations()
st.selectbox("", options=locations, placeholder="Selecione um local",
             format_func=lambda l: l["nome"], key="location_selectbox", index=None)

if (local := st.session_state.get("location_selectbox")):
    uploaded_file = st.file_uploader(
        "Carregar imagem", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Ler os bytes
        bytes_data = uploaded_file.read()

        if len(bytes_data):
            # Mostrar preview
            st.image(bytes_data)

            # Dados para registro no banco de dados
            local_image_data = {
                "id_arquivo": None,
                "local_lat": local["lat"],
                "local_lng": local["lng"],
                "nome_arquivo": uploaded_file.name,
                "tipo": uploaded_file.type,
                "tamanho": uploaded_file.size,
                "conteudo": b64encode(bytes_data).decode("utf8"),
                "data_upload": datetime.now().strftime("%Y-%m-%d")
            }

            if st.button("Enviar"):
                st.session_state.upload_image_result = upload_location_image(local_image_data)
                if st.session_state.upload_image_result:
                    st.rerun()
