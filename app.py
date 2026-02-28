import streamlit as st
import numpy as np

st.set_page_config(page_title="Bet Analyzer", page_icon="⚽")

st.title("⚽ Bet Analyzer")

local = st.text_input("Equipo Local")
visitante = st.text_input("Equipo Visitante")

cuota = st.number_input("Cuota", min_value=1.01, step=0.01)
prob = st.slider("Probabilidad estimada (%)", 1, 99, 50)

if st.button("Calcular Valor"):
    
    prob_decimal = prob / 100
    prob_imp = 1 / cuota
    edge = prob_decimal - prob_imp
    
    st.write("Probabilidad implícita:", round(prob_imp*100,2), "%")
    st.write("Edge:", round(edge*100,2), "%")
    
    if edge > 0:
        st.success("✅ Hay valor")
    else:
        st.error("❌ No hay valor")
