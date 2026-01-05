import streamlit as st
import gspread
import pytz
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Mi Billetera", page_icon="💰")

# --- CONEXIÓN SEGURA A GOOGLE SHEETS ---
def conectar_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Intenta leer desde los Secrets (para la Web)
    if "gcp_service_account" in st.secrets:
        creds_dict = st.secrets["gcp_service_account"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    else:
        # Si no hay secrets, usa el archivo local (para pruebas en tu PC)
        creds = ServiceAccountCredentials.from_json_keyfile_name("credenciales.json", scope)
        
    client = gspread.authorize(creds)
    return client.open_by_key("1n6aPZQ_DVw22wuQqYotnQ_EEU8l6TowgyOE-vE2agFs").sheet1

try:
    sheet = conectar_google_sheets()
except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.stop()

# --- INTERFAZ GRÁFICA (LO QUE VERÁS EN EL MÓVIL) ---
st.title("💰 Registro de Gastos")
st.markdown("Completa los datos y presiona guardar.")

with st.form("registro_movil", clear_on_submit=True):
    # Casillas de entrada
    descripcion = st.text_input("¿En qué gastaste?", placeholder="Ej: Almuerzo corrientazo")
    monto = st.number_input("Monto (COP)", min_value=0, step=1000)
    
    categoria = st.selectbox("Categoría", [
        "Gastos Fijos (55%)", 
        "Ahorro/Inversión (30%)", 
        "Gustos (15%)"
    ])
    
    # Botón grande para el pulgar en el móvil
    boton_guardar = st.form_submit_button("Añadir Gasto", use_container_width=True)

if boton_guardar:
    if descripcion and monto > 0:
        # Obtener fecha y hora de Colombia
        tz = pytz.timezone('America/Bogota')
        ahora = datetime.now(tz)
        
        # Preparar la fila
        nueva_fila = [
            ahora.strftime("%d/%m/%Y"), 
            ahora.strftime("%H:%M:%S"), 
            descripcion, 
            categoria, 
            monto
        ]
        
        # Guardar en Drive
        with st.spinner("Guardando..."):
            sheet.append_row(nueva_fila)
        
        st.success(f"✅ Registrado: {descripcion}")
        st.balloons()
    else:
        st.warning("Escribe una descripción y un monto.")