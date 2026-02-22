import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

# Inicializar estado
if "pantalla" not in st.session_state:
    st.session_state.pantalla = ""
if "historial" not in st.session_state:
    st.session_state.historial = []

# CSS para mejorar los botones
st.markdown("""
<style>
div.stButton > button {
    font-size: 22px !important;
    height: 60px !important;
    width: 100% !important;
    border-radius: 8px !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 Calculadora Virtual")
st.markdown("---")

# Pantalla
valor_pantalla = st.session_state.pantalla if st.session_state.pantalla else "0"
st.markdown(f"""
    <div style='background:#1e1e1e; padding:20px; border-radius:10px;
    font-size:36px; text-align:left; color:white; min-height:70px; margin-bottom:15px;'>
    {valor_pantalla}
    </div>
""", unsafe_allow_html=True)

# Funciones
def presionar(v):
    st.session_state.pantalla += v

def limpiar():
    st.session_state.pantalla = ""

def borrar():
    st.session_state.pantalla = st.session_state.pantalla[:-1]

def calcular():
    try:
        exp = st.session_state.pantalla
        res = str(eval(exp))
        st.session_state.historial.append(f"{exp} = {res}")
        st.session_state.pantalla = res
    except:
        st.session_state.pantalla = "Error"

# Fila 1
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("C",   key="btn_c"):  limpiar()
with c2:
    if st.button("DEL", key="btn_del"): borrar()
with c3:
    if st.button("%",   key="btn_pct"): presionar("%")
with c4:
    if st.button("/",   key="btn_div"): presionar("/")

# Fila 2
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("7", key="btn_7"): presionar("7")
with c2:
    if st.button("8", key="btn_8"): presionar("8")
with c3:
    if st.button("9", key="btn_9"): presionar("9")
with c4:
    if st.button("*", key="btn_mul"): presionar("*")

# Fila 3
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("4", key="btn_4"): presionar("4")
with c2:
    if st.button("5", key="btn_5"): presionar("5")
with c3:
    if st.button("6", key="btn_6"): presionar("6")
with c4:
    if st.button("-", key="btn_min"): presionar("-")

# Fila 4
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("1", key="btn_1"): presionar("1")
with c2:
    if st.button("2", key="btn_2"): presionar("2")
with c3:
    if st.button("3", key="btn_3"): presionar("3")
with c4:
    if st.button("+", key="btn_sum"): presionar("+")

# Fila 5
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("0", key="btn_0"): presionar("0")
with c2:
    if st.button(".", key="btn_dot"): presionar(".")
with c3:
    st.write("")  # espacio vacío
with c4:
    if st.button("=", key="btn_eq"): calcular()

# Historial
if st.session_state.historial:
    st.markdown("---")
    st.markdown("### 📋 Historial")
    for op in reversed(st.session_state.historial[-5:]):
        st.write(op)
