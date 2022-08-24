# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:19:54 2022

@author: mjkipsz2
"""

import streamlit as st
import numpy as np
import pandas as pd


st.title("Calculo de la huella de carbono industrial")

df=pd.read_csv('emission factors.csv')

fuels=df['fuel_name']

fuels=st.multiselect('Fuel',fuels)
fuel_names=pd.DataFrame(fuels).transpose()
st.write(fuel_names)

# Mask to filter dataframe
mask_fuels = df['fuel_name'].isin(fuels)

df = df[mask_fuels]
df.drop(['heat_content','unit_heat_content'],axis=1,inplace=True)
st.write(df)

df0=[]


#fuel_selection=st.selectbox('Fuel',fuels)
for i in fuels:
    fuel_consumption=st.number_input("Enter fuel consumption",min_value=1,key=i)

if st.button("Add row"):
    df0.append({"Fuel": fuels, "consumption": fuel_consumption})
    st.write(pd.DataFrame(df0))

 
if st.button('Delete'):
    del df0
    



