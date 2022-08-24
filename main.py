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

fuel_selection=st.multiselect('Fuel',fuels)

# Mask to filter dataframe
mask_fuels = df['fuel_name'].isin(fuel_selection)

data = data[mask_fuels]
