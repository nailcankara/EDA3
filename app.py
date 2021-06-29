import streamlit as st
from multiapp import MultiApp
from apps import home , VeriGorsellestirme

app = MultiApp()

st.image('./fibabanka-logo.png')
st.markdown("UYGULAMALAR")

app.add_app("Home", home.app)
app.add_app("Veri Görselleştirme", VeriGorsellestirme.app)

app.run()
