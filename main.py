# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:19:54 2022

@author: mjkipsz2
"""

import streamlit as st
import numpy as np
import pandas as pd

st.title("Calculo de la huella de carbono industrial")

df = pd.read_excel("emission factors.xlsx")

fuel_names=df['fuel_name']

st.multiselect('Seleccione los combustibles',fuel_names)


