import streamlit as st
import requests
import base64

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

# Función de conexión corregida (Lee la clave segura de Streamlit y apunta a OpenRouter)
def analizar_imagen_real(prompt_texto, campo_foto):
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    # Chupa tu clave "sk-or-v1..." directo de la caja fuerte de Streamlit
    llave_openrouter = st.secrets["GEMINI_API_KEY"]
    
    headers = {
        "Authorization": f"Bearer {llave_openrouter}",
        "Content-Type": "application/json"
    }
    
    # Convertir la foto para el viaje por el módem
    bytes_data = campo_foto.getvalue()
    base64_image = base64.b64encode(bytes_data).decode('utf-8')
    
    payload = {
        # Modelo de Google Gemini 1.5 Flash GRATUITO adentro de OpenRouter
        "model": "google/gemini-flash-1.5",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_texto},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error del servidor OpenRouter ({response.status_code}): {response.text}"

# 2. INTERFAZ OPERATIVA EXCLUSIVA
st.markdown("<h2>ANALIZADOR DE PIEL</h2>", unsafe_allow_html=True)
opcion = st.radio("Cargar rostro mediante:", ["📸 Usar Cámara del Celu", "🖼️ Subir de Galería"], horizontal=True)

foto = st.camera_input("Capturá el rostro") if opcion == "📸 Usar Cámara del Celu" else st.file_uploader("Seleccioná una imagen", type=['jpg', 'png', 'jpeg'])

if foto:
    if st.button("🚀 INICIAR DIAGNÓSTICO"):
        with st.spinner("Analizando la imagen real en vivo..."):
            try:
                prompt = ("Actúa como un sistema avanzado de diagnóstico dermatocosmético para profesionales. "
                          "Analiza la piel de la imagen adjunta de forma científica. "
                          "Estructura tu respuesta usando exactamente estos títulos: "
                          "### 1) BIOTIPO CUTÁNEO (Describe detalladamente las zonas del rostro)\n\n"
                          "### 2) FOTOTIPO (Determina la Escala Fitzpatrick según los rasgos visibles)\n\n"
                          "### 3) CONDICIONES / LESIONES VISIBLES (Detalla líneas de expresión, manchas o sensibilidad sin sugerir marcas comerciales).")
                
                resultado = analizar_imagen_real(prompt, foto)
                st.markdown(f"<div style='background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #d81b60; color: black;'>{resultado}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Falla en la conexión de datos: {e}. Intentá sacar la foto de nuevo.")

st.markdown("---")
st.caption("Gestión Técnico-Analógica Internacional: Fabio & Olga — CEI 2026")
