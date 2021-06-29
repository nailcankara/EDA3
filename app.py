import streamlit as st
from multiapp import MultiApp
from apps import home , VeriGorsellestirme

app = MultiApp()

st.markdown("UYGULAMALAR")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Veri Görselleştirme", VeriAnaliziFinal.app)
# The main app
app.run()
