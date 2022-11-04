import streamlit as st

#Codigo para eliminar el boton de menu y logo de streamlit
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("# Contacto")

contact_form = """
<form action="https://formsubmit.co/zapaz.consultores@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="Nombre" placeholder="Tu nombre" required>
     <input type="email" name="email" placeholder="Tu email" required>
     <textarea name="message" placeholder="Tu mensaje"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
