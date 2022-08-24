# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:19:54 2022

@author: mjkipsz2
"""

import streamlit as st
import numpy as np
import pandas as pd

@st.cache(allow_output_mutation=True)
def get_data():
    return []

st.title("Calculo de la huella de carbono industrial")

df=pd.read_csv('emission factors.csv')

fuels=df['fuel_name']

fuels=st.multiselect('Fuel',fuels)

# Mask to filter dataframe
mask_fuels = df['fuel_name'].isin(fuels)

df = df[mask_fuels]
df.drop(['heat_content','unit_heat_content'],axis=1,inplace=True)
st.write(df)


fuel_selection=st.selectbox('Fuel',fuels)
fuel_consumption=st.number_input("Enter fuel consumption",min_value=1)

if st.button("Add row"):
    get_data().append({"Fuel": fuel_selection, "consumption": fuel_consumption})

data=pd.DataFrame(get_data)      
st.write(data)

 
if st.button('Delete'):
    del data
    st.write('mr button has delet for u')
    
try:
    st.write(pd.DataFrame(data=data))
except:
    pass 



