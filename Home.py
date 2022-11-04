# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:19:54 2022

@author: mjkipsz2
"""

import streamlit as st

st.set_page_config(layout="wide",page_title="AUCAF",page_icon="🌿")

#Codigo para eliminar el boton de menu y logo de streamlit
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

from PIL import Image
image = Image.open('Resources/logo_Pungo.png')
st.image(image)

st.write("# Bienvenido al demo de AUCAF: la herramienta digital para el cálculo, monitoreo y reducción de la huella de carbono en la industria")
