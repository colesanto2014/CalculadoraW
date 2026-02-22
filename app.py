import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")
st.title("🧮 Calculadora Virtual")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    background: transparent;
    margin: 0;
  }
  .calc {
    background: #1e1e2e;
    border-radius: 16px;
    padding: 20px;
    width: 300px;
  }
  #pantalla {
    background: #313244;
    color: white;
    font-size: 32px;
    text-align: left;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 15px;
    min-height: 55px;
    word-break: break-all;
  }
  .fila {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-bottom: 10px;
  }
  button {
    padding: 18px;
    font-size: 20px;
    font-weight: bold;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    color: white;
    background: #45475a;
    transition: background 0.1s;
  }
  button:active { opacity: 0.7; }
  .op  { background: #89b4fa; color: #1e1e2e; }
  .eq  { background: #a6e3a1; color: #1e1e2e; }
  .del { background: #f38ba8; color: #1e1e2e; }
</style>
</head>
<body>
<div class="calc">
  <div id="pantalla">0</div>

  <div class="fila">
    <button class="del" onclick="limpiar()">C</button>
    <button class="del" onclick="borrar()">DEL</button>
    <button class="op"  onclick="agregar('%')">%</button>
    <button class="op"  onclick="agregar('/')">÷</button>
  </div>
  <div class="fila">
    <button onclick="agregar('7')">7</button>
    <button onclick="agregar('8')">8</button>
    <button onclick="agregar('9')">9</button>
    <button class="op" onclick="agregar('*')">×</button>
  </div>
  <div class="fila">
    <button onclick="agregar('4')">4</button>
    <button onclick="agregar('5')">5</button>
    <button onclick="agregar('6')">6</button>
    <button class="op" onclick="agregar('-')">-</button>
  </div>
  <div class="fila">
    <button onclick="agregar('1')">1</button>
    <button onclick="agregar('2')">2</button>
    <button onclick="agregar('3')">3</button>
    <button class="op" onclick="agregar('+')">+</button>
  </div>
  <div class="fila">
    <button onclick="agregar('0')" style="grid-column: span 2;">0</button>
    <button onclick="agregar('.')">.</button>
    <button class="eq" onclick="calcular()">=</button>
  </div>
</div>

<script>
  let expresion = "";

  function actualizar() {
    document.getElementById("pantalla").innerText = expresion || "0";
  }

  function agregar(valor) {
    expresion += valor;
    actualizar();
  }

  function limpiar() {
    expresion = "";
    actualizar();
  }

  function borrar() {
    expresion = expresion.slice(0, -1);
    actualizar();
  }

  function calcular() {
    try {
      expresion = String(eval(expresion));
    } catch {
      expresion = "Error";
    }
    actualizar();
  }
</script>
</body>
</html>
""", height=500)
