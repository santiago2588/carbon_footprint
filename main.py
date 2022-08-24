# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:19:54 2022

@author: mjkipsz2
"""

import streamlit as st
import numpy as np
import pandas as pd

st.title("Calculo de la huella de carbono industrial")

excel_file='emission factors.xlsx'

df=pd.read_excel(excel_file)

fuels=df['fuel_name'].tolist()

fuel_selection=st.multiselect('Fuel',fuels)
