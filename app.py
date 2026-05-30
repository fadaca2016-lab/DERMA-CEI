import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. ESTÉTICA PROFESIONAL EN ROSA CEI
st.set_page_config(page_title="Derma CEI v11.0", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #fff0f5; }
    .stButton>button { 
        background-color: #d81b60; color: white; 
        border-radius: 20px; width: 100%; border: none; font-weight: bold; height: 3.5em;
    }
    .stButton>button:hover { background-color: #ff69b4; color: white; }
    h1, h2 { color: #d81b60; text-align: center; font-family: 'Helvetica Neue', Arial, sans-serif; }
    .stRadio > label { color: #ad1457; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>derma-cei</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ad1457;'>Cosmiatra de Bolsillo - Motor Original</p>", unsafe_allow_html=True)
st.markdown("---")

# 2. CONEXIÓN SEGURA DESDE LA CAJA FUERTE (Secrets)
try:
    # Va a buscar la llave de forma oculta a la configuración de la nube de Streamlit
    api_key_segura = st.secrets["AQ.Ab8RN6LHyAZ5ME30_-A-GthtvTIFEF7aKMM5Ezkh03Q4uigBSQ"]
    genai.configure(api_key=api_key_segura)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ Falta configurar la llave de paso (GEMINI_API_KEY) en los Secrets de Streamlit.")
    model = None

# 3. INTERFAZ OPERATIVA EXCLUSIVA
st.markdown("<h2>ANALIZADOR DE PIEL</h2>", unsafe_allow_html=True)
opcion = st.radio("Cargar rostro mediante:", ["📸 Usar Cámara del Celu", "🖼️ Subir de Galería"], horizontal=True)

foto = st.camera_input("Capturá el rostro") if opcion == "📸 Usar Cámara del Celu" else st.file_uploader("Seleccioná una imagen", type=['jpg', 'png', 'jpeg'])

if foto and model:
    if st.button("🚀 INICIAR DIAGNÓSTICO"):
        with st.spinner("Analizando la imagen real con Gemini 1.5..."):
            try:
                img = Image.open(foto)
                prompt = ("Actúa como un sistema avanzado de diagnóstico dermatocosmético para profesionales. "
                          "Analiza la piel de la imagen de forma científica y real. "
                          "Estructura tu respuesta usando exactamente estos títulos: "
                          "### 1) BIOTIPO CUTÁNEO\n\n"
                          "### 2) FOTOTIPO (Escala Fitzpatrick)\n\n"
                          "### 3) CONDICIONES / LESIONES VISIBLES.\n\n"
                          "Describe detalladamente el tejido sin sugerir marcas comerciales.")
                
                response = model.generate_content([prompt, img])
                st.markdown(f"<div style='background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #d81b60; color: black;'>{response.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Falla en el análisis: {e}")

st.markdown("---")
st.caption("Gestión Técnico-Analógica de Precisión: Fabio & Olga — CEI 2026")
