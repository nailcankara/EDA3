import streamlit as st
from multiapp import MultiApp
from apps import home , VeriAnaliziFinal

app = MultiApp()

st.image('./fibabanka-logo.png')
st.markdown("UYGULAMALAR")

app.add_app("Home", home.app)
app.add_app("Veri Görselleştirme", VeriAnaliziFinal.app)

app.run()
