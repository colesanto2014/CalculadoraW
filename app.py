import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

st.title("🧮 Calculadora Virtual")
st.markdown("---")

# Historial de operaciones
if "historial" not in st.session_state:
    st.session_state.historial = []

if "pantalla" not in st.session_state:
    st.session_state.pantalla = ""

# Pantalla
pantalla = st.text_input("", value=st.session_state.pantalla, key="display",
                          placeholder="0", label_visibility="collapsed")

st.markdown("###")

# Botones
col1, col2, col3, col4 = st.columns(4)

def agregar(valor):
    st.session_state.pantalla += valor

def limpiar():
    st.session_state.pantalla = ""

def borrar():
    st.session_state.pantalla = st.session_state.pantalla[:-1]

def calcular():
    try:
        expresion = st.session_state.pantalla
        resultado = str(eval(expresion))
        st.session_state.historial.append(f"{expresion} = {resultado}")
        st.session_state.pantalla = resultado
    except:
        st.session_state.pantalla = "Error"

with col1:
    if st.button("C", use_container_width=True):       limpiar()
    if st.button("7", use_container_width=True):       agregar("7")
    if st.button("4", use_container_width=True):       agregar("4")
    if st.button("1", use_container_width=True):       agregar("1")
    if st.button("0", use_container_width=True):       agregar("0")

with col2:
    if st.button("⌫", use_container_width=True):      borrar()
    if st.button("8", use_container_width=True):       agregar("8")
    if st.button("5", use_container_width=True):       agregar("5")
    if st.button("2", use_container_width=True):       agregar("2")
    if st.button(".", use_container_width=True):       agregar(".")

with col3:
    if st.button("%", use_container_width=True):       agregar("%")
    if st.button("9", use_container_width=True):       agregar("9")
    if st.button("6", use_container_width=True):       agregar("6")
    if st.button("3", use_container_width=True):       agregar("3")
    if st.button("=", use_container_width=True):       calcular()

with col4:
    if st.button("÷", use_container_width=True):       agregar("/")
    if st.button("×", use_container_width=True):       agregar("*")
    if st.button("-", use_container_width=True):       agregar("-")
    if st.button("+", use_container_width=True):       agregar("+")

# Historial
if st.session_state.historial:
    st.markdown("---")
    st.markdown("### 📋 Historial")
    for op in reversed(st.session_state.historial[-5:]):
        st.write(op)
