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

fuel_selection=st.selectbox('Fuel',fuels)
fuel_consumption=st.number_input("Enter fuel consumption",min_value=1)

if st.button("Add row"):
    get_data().append({"Fuel": fuel_selection, "consumption": fuel_consumption})

st.write(pd.DataFrame(get_data()))

#for fuel in fuel_selection:
  #fuel_consumption=st.number_input("Enter fuel consumption",min_value=1,key=fuel)
  
  
# Mask to filter dataframe
#mask_fuels = df['fuel_name'].isin(fuel_selection)

#df = df[mask_fuels]
#df.drop(['heat_content','unit_heat_content'],axis=1,inplace=True)
#df.concat(fuel_consumption,axis=1)
#st.write(df)


