# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:19:54 2022

@author: mjkipsz2
"""

import streamlit as st
import equations
import base64

st.title(' ')
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
       data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
        <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
        ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('background.png')


st.title("Calculo de la huella de carbono industrial")
option = st.selectbox(
    'Selecciona el tipo de emisiones de carbono que deseas calcular',
    ('Selecciona una opcion', 'Combustion fuentes fijas','Combustion fuentes moviles','Electricidad'))

if option=="Combustion fuentes fijas":
        equations.household()
elif option=="Combustion fuentes moviles":
        equations.publictransport()
elif option=="Electricidad":
        equations.carcarbonfootprint()
