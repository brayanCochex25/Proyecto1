{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a6a76a01",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-01-05 14:38:18.127 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.127 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.129 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.131 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.131 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.133 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.134 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.135 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.136 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.138 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.138 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.140 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.143 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.145 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.146 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.147 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.150 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.150 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.153 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.154 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.158 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.159 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.161 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.162 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.163 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.165 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.165 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.167 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.168 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-05 14:38:18.170 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import gspread\n",
    "from datetime import datetime\n",
    "import pytz # Librería para zonas horarias\n",
    "from oauth2client.service_account import ServiceAccountCredentials\n",
    "import os\n",
    "\n",
    "ruta_base = r\"J:/Mi unidad/API_FINANZAS\"\n",
    "os.chdir(ruta_base)\n",
    "os.getcwd()\n",
    "\n",
    "# --- CONFIGURACIÓN DE GOOGLE SHEETS ---\n",
    "scope = [\"https://spreadsheets.google.com/feeds\", \"https://www.googleapis.com/auth/drive\"]\n",
    "creds = ServiceAccountCredentials.from_json_keyfile_name(\"credenciales.json\", scope)\n",
    "client = gspread.authorize(creds)\n",
    "sheet = client.open(\"ANEXO_GASTOS\").sheet1\n",
    "\n",
    "\n",
    "# --- INTERFAZ DE LA APP ---\n",
    "# Ejemplo de mejoras en el formulario\n",
    "st.title(\"💰 Mi Gestor de Finanzas (Colombia)\")\n",
    "\n",
    "with st.form(\"registro_gasto\"):\n",
    "    desc = st.text_input(\"¿Qué compraste?\")\n",
    "    monto = st.number_input(\"Valor en COP\", min_value=0, step=500)\n",
    "    \n",
    "    # Aquí puedes usar tus porcentajes definidos al inicio\n",
    "    cat = st.selectbox(\"Distribución\", [\n",
    "        \"Gastos Fijos/Variables (55%)\",\n",
    "        \"Ahorro/Inversión (30%)\",\n",
    "        \"Gustos Personales (15%)\"\n",
    "    ])\n",
    "    \n",
    "    enviar = st.form_submit_button(\"Guardar Gasto\")\n",
    "\n",
    "if enviar:\n",
    "    if desc and monto > 0:\n",
    "        # 1. Obtener Hora Colombia\n",
    "        zona_horaria_col = pytz.timezone('America/Bogota')\n",
    "        ahora_col = datetime.now(zona_horaria_col)\n",
    "        \n",
    "        fecha_str = ahora_col.strftime(\"%d/%m/%Y\")\n",
    "        hora_str = ahora_col.strftime(\"%H:%M:%S\")\n",
    "        \n",
    "        # 2. Preparar la fila con los nombres de variables correctos\n",
    "        nueva_fila = [fecha_str, hora_str, desc, cat, monto]\n",
    "        \n",
    "        # 3. Anexar al final\n",
    "        with st.spinner(\"Guardando en la nube...\"):\n",
    "            sheet.append_row(nueva_fila)\n",
    "        \n",
    "        st.success(f\"✅ ¡Guardado! {desc} por ${monto:,.0f} a las {hora_str}\")\n",
    "        st.balloons()\n",
    "    else:\n",
    "        st.warning(\"Por favor escribe una descripción y un monto válido.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7edc726d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install streamlit gspread oauth2client pytz"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
