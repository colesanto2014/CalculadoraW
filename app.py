import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

# Inicializar estado
if "pantalla" not in st.session_state:
    st.session_state.pantalla = ""

st.title("🧮 Calculadora Virtual")
st.markdown("---")

# Pantalla
valor = st.session_state.pantalla if st.session_state.pantalla else "0"
st.markdown(f"""
    <div style='background:#1e1e1e; padding:20px; border-radius:10px;
    font-size:36px; text-align:left; color:white; min-height:65px; margin-bottom:15px;'>
    {valor}
    </div>
""", unsafe_allow_html=True)

# Función central
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

# Botones organizados por filas
botones = [
    ["C", "DEL", "%", "/"],
    ["7", "8",   "9", "*"],
    ["4", "5",   "6", "-"],
    ["1", "2",   "3", "+"],
    ["0", ".",   "="],
]

for fila in botones:
    cols = st.columns(len(fila))
    for i, simbolo in enumerate(fila):
        with cols[i]:
            if st.button(simbolo, key=f"btn_{simbolo}", use_container_width=True):
                accion(simbolo)
                st.rerun()
