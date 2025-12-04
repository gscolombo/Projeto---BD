import streamlit as st
import psycopg2

st.title("Upload de imagem para Local")

uploaded_file = st.file_uploader("Carregar imagem", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Ler os bytes
    bytes_data = uploaded_file.read()

    # Mostrar preview
    st.image(bytes_data, caption="Preview")

    try:
        conn = psycopg2.connect(
            dbname="detran",
            user="postgres",
            password="12345",
            host="localhost",
            port="5432"
        )
        conn.set_client_encoding("UTF8")
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO local_arquivo (lat, lng, nome_arquivo, tipo, tamanho, conteudo)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            -15.7801,
            -47.9292,            #lat e long fixo para teste
            "algo.png",          # nome fixo para teste
            "teste/png",         # tipo fixo para teste
            len(bytes_data),
            psycopg2.Binary(bytes_data)
        ))

        conn.commit()
        cur.close()
        conn.close()
        st.success("Imagem salva no banco com sucesso!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco: {e}")
