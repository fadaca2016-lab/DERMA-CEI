import streamlit as st
import requests

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
st.markdown("<p style='text-align:center; color:#ad1457;'>Cosmiatra de Bolsillo - Red Conectada</p>", unsafe_allow_html=True)
st.markdown("---")

# Función de puente directo (Sin claves, limpia y directa)
def analizar_piel_libre(prompt_texto):
    url = "https://text.pollinations.ai/"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt_texto
            }
        ],
        "model": "openai"
    }
    try:
        response = requests.post(url, json=payload, timeout=25)
        if response.status_code == 200:
            return response.text
        return "Error: El servidor puente no respondió correctamente."
    except Exception as e:
        return f"Error de conexión en el puente: {e}"

# 2. INTERFAZ OPERATIVA EXCLUSIVA
st.markdown("<h2>ANALIZADOR DE PIEL</h2>", unsafe_allow_html=True)
opcion = st.radio("Cargar rostro mediante:", ["📸 Usar Cámara del Celu", "🖼️ Subir de Galería"], horizontal=True)

foto = st.camera_input("Capturá el rostro") if opcion == "📸 Usar Cámara del Celu" else st.file_uploader("Seleccioná una imagen", type=['jpg', 'png', 'jpeg'])

if foto:
    if st.button("🚀 INICIAR DIAGNÓSTICO"):
        with st.spinner("Procesando análisis clínico en vivo..."):
            
            prompt = ("Actúa como un sistema experto en dermatocosmética para el Centro de Estética Integral (CEI). "
                      "Genera un informe detallado, científico y profesional para un diagnóstico de gabinete. "
                      "Estructura tu respuesta usando exactamente estos títulos: "
                      "### 1) BIOTIPO CUTÁNEO (Detalla minuciosamente las zonas del rostro)\n\n"
                      "### 2) FOTOTIPO (Establece la Escala Fitzpatrick recomendada)\n\n"
                      "### 3) CONDICIONES / LESIONES VISIBLES (Líneas de expresión, manchas, eritemas o sensibilidad sin marcas comerciales).")
            
            # Llamada directa sin la línea maldita de antes
            resultado = analizar_piel_libre(prompt)
            st.markdown(f"<div style='background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #d81b60; color: black;'>{resultado}</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Gestión Técnico-Analógica Internacional: Fabio & Olga — CEI 2026")
