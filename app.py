import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

st.title("🧮 Calculadora Virtual")
st.markdown("---")

# Inicializar estado
if "pantalla" not in st.session_state:
    st.session_state.pantalla = ""
if "historial" not in st.session_state:
    st.session_state.historial = []

# Pantalla - texto a la IZQUIERDA
st.markdown(f"""
    <div style='background-color:#1e1e1e; padding:20px; border-radius:10px;
    font-size:32px; text-align:left; color:white; min-height:60px; margin-bottom:20px;'>
    {st.session_state.pantalla if st.session_state.pantalla else "0"}
    </div>
""", unsafe_allow_html=True)

# Funciones
def presionar(valor):
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

# Botones — se usan claves únicas para evitar conflictos
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("C",    key="c",   use_container_width=True): limpiar()
    if st.button("7",    key="n7",  use_container_width=True): presionar("7")
    if st.button("4",    key="n4",  use_container_width=True): presionar("4")
    if st.button("1",    key="n1",  use_container_width=True): presionar("1")
    if st.button("0",    key="n0",  use_container_width=True): presionar("0")

with col2:
    if st.button("⌫",   key="bk",  use_container_width=True): borrar()
    if st.button("8",    key="n8",  use_container_width=True): presionar("8")
    if st.button("5",    key="n5",  use_container_width=True): presionar("5")
    if st.button("2",    key="n2",  use_container_width=True): presionar("2")
    if st.button(".",    key="pt",  use_container_width=True): presionar(".")

with col3:
    if st.button("%",    key="pc",  use_container_width=True): presionar("%")
    if st.button("9",    key="n9",  use_container_width=True): presionar("9")
    if st.button("6",    key="n6",  use_container_width=True): presionar("6")
    if st.button("3",    key="n3",  use_container_width=True): presionar("3")
    if st.button("=",    key="eq",  use_container_width=True): calcular()

with col4:
    if st.button("÷",   key="dv",  use_container_width=True): presionar("/")
    if st.button("×",   key="ml",  use_container_width=True): presionar("*")
    if st.button("-",    key="mn",  use_container_width=True): presionar("-")
    if st.button("+",    key="pl",  use_container_width=True): presionar("+")

# Historial
if st.session_state.historial:
    st.markdown("---")
    st.markdown("### 📋 Historial")
    for op in reversed(st.session_state.historial[-5:]):
        st.write(op)
