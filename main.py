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
fuel_names=pd.DataFrame(fuels)

# Mask to filter dataframe
mask_fuels = df['fuel_name'].isin(fuels)

df = df[mask_fuels]
df.drop(['heat_content','unit_heat_content'],axis=1,inplace=True)
st.write(df)

df0=[]

for i in fuels:
    #fuel_name=st.selectbox("Enter fuel name",fuels,key=i)
    fuel_consumption=st.number_input(str(i)+"consumption",min_value=1,key=i)
    df0.append({"Consumption": fuel_consumption})

fuel_con=pd.DataFrame(df0)

results=pd.concat([fuel_names,fuel_con],axis='columns')
    
if st.button("Add row"):
    st.write(results)

 
if st.button('Delete'):
    del results
    



