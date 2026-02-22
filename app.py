import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

# ============================
#    ESTILOS PROFESIONALES
# ============================
st.markdown("""
<style>

button[kind="secondary"] {
    background-color: #333 !important;
    border-radius: 10px !important;
    border: 1px solid #555 !important;
    font-size: 22px !important;
    height: 65px !important;
    margin: 4px 0 !important;
}

/* CORRECCIÓN CRÍTICA:
   Esto hace que el texto (+, -, *) sea visible */
button[kind="secondary"] > div > p {
    color: white !important;
    font-weight: 600 !important;
}

button[kind="secondary"]:hover {
    background-color: #444 !important;
    border-color: #777 !important;
}

</style>
""", unsafe_allow_html=True)

# ============================
#   ESTADO
# ============================
if "pantalla" not in st.session_state:
    st.session_state.pantalla = ""

st.title("🧮 Calculadora Virtual V5")
st.markdown("---")

# ============================
#   PANTALLA
# ============================
valor = st.session_state.pantalla if st.session_state.pantalla else "0"

st.markdown(f"""
    <div style='background:#1e1e1e; padding:20px; border-radius:10px;
    font-size:36px; text-align:right; color:white; min-height:65px; margin-bottom:15px;'>
    {valor}
    </div>
""", unsafe_allow_html=True)

# ============================
#   FUNCIÓN CENTRAL
# ============================
def accion(tipo):
    if tipo == "C":
        st.session_state.pantalla = ""
    elif tipo == "DEL":
        st.session_state.pantalla = st.session_state.pantalla[:-1]
    elif tipo == "=":
        try:
            st.session_state.pantalla = str(eval(st.session_state.pantalla))
        except:
            st.session_state.pantalla = "Error"
    else:
        st.session_state.pantalla += tipo

# ============================
#   BOTONES
# ============================
botones = [
    ["C", "DEL", "%", "/"],
    ["7", "8",   "9", "*"],
    ["4", "5",   "6", "-"],
    ["1", "2",   "3", "+"],
    ["0", ".",   "="],
]

def clave_segura(simbolo):
    reemplazos = {
        "+": "plus",
        "-": "minus",
        "*": "mul",
        "/": "div",
        "%": "percent",
        "=": "equal",
        ".": "dot"
    }
    return reemplazos.get(simbolo, simbolo)

for fila in botones:
    cols = st.columns(len(fila))
    for i, simbolo in enumerate(fila):
        key_segura = f"btn_{clave_segura(simbolo)}"
        with cols[i]:
            if st.button(simbolo, key=key_segura, use_container_width=True, type="secondary"):
                accion(simbolo)
                st.rerun()
