import streamlit as st
from apps import home , VeriGorsellestirme

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title,"function": func})

    def run(self):
        app = st.selectbox(
            'Navigasyon',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()


app = MultiApp()

st.image('./fibabanka-logo.png')
st.subheader("UYGULAMALAR")

app.add_app("Home", home.app)
app.add_app("Veri Görselleştirme", VeriGorsellestirme.app)

app.run()
