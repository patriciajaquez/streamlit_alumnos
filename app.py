import streamlit as st
import pandas as pd
import plotly.express as px

#-------------------------------------------------------------------------------------------
# Configuración de la página
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon=":tada:",
    layout="wide"
)

#-------------------------------------------------------------------------------------------
# CSS personalizado
st.markdown("""
    <style>
        /* Importa una fuente de Google */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }

        /* Estilo principal de la app */
        .main {
            padding: 2rem;
            background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
        }

        /* Encabezados principales */
        .css-10trblm, h1, h2, h3 {
            color: #1E88E5;
            border-bottom: 2px solid #1E88E5;
            padding-bottom: 0.3rem;
            margin-bottom: 1rem;
        }

        /* Sidebar estilizado */
        [data-testid="stSidebar"] {
            background-color: #ffffff;
            padding: 2rem 1rem;
            border-right: 1px solid #e0e0e0;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p {
            margin: 0.5rem 0;
        }

        /* Pestañas */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
            margin-bottom: 1rem;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #f1f5f9;
        }

        /* Estilo de las columnas para una apariencia tipo "card" */
        .stColumn {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 0.5rem;
        }

        /* Estilos personalizados para alertas e información */
        .stAlert {
            border-radius: 6px;
            padding: 1rem;
            margin: 0.5rem 0;
            background-color: #f0f4f8;
            border-left: 4px solid #1E88E5;
        }
    </style>
""", unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------
# Sidebar con una imagen y contenido HTML actualizado
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", 
                caption="Streamlit logo",
                width=200)
st.sidebar.markdown("""
    <div style='background-color:#ffffff; padding: 1.5rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h1>Sidebar</h1>
        <h2>Encabezado</h2>
        <h3>Subencabezado</h3>
        <p>¡Bienvenido/a!</p>
    </div>
""", unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------
# Definición de pestañas
tab1, tab2, tab3 = st.tabs(["📝 Text", "🎥 Media & Resources", "📊 Dataframe"])

with tab1:
    st.title("My First Streamlit App")
    st.header("Encabezado Principal")
    st.subheader("Subencabezado Secundario")
    st.text("Hola, Mundo!")
    st.markdown("## Encabezado en Markdown")
    st.markdown("Este es un **subtitulo** en Markdown")
    st.latex(r"""a^2 + b^2 = c^2""")
    st.code("print('Hola, Mundo!')", language="python")
    st.info("Mensaje de información")
    st.warning("Mensaje de advertencia")
    st.error("Mensaje de error")
    st.success("Mensaje de éxito")
    st.exception("Mensaje de excepción")

with tab2:
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit logo")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

with tab3:
    df = pd.DataFrame({
        'Columna 1': [1, 2, 3, 8],
        'Columna 2': [4, 5, 6, 15],
        'Columna 3': [7, 8, 9, 22]
    })
    st.dataframe(df)

#-------------------------------------------------------------------------------------------
# Columnas con estilo tipo "card"
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='stColumn'>"
                "<img src='https://www.streamlit.io/images/brand/streamlit-mark-color.png' width='100%'>"
                "<p style='text-align: center;'>Streamlit logo</p>"
                "</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='stColumn'>"
                "<img src='https://www.streamlit.io/images/brand/streamlit-mark-color.png' width='100%'>"
                "<p style='text-align: center;'>Streamlit logo</p>"
                "</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='stColumn'>"
                "<img src='https://www.streamlit.io/images/brand/streamlit-mark-color.png' width='100%'>"
                "<p style='text-align: center;'>Streamlit logo</p>"
                "</div>", unsafe_allow_html=True)
