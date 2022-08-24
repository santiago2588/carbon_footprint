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

#Calculo de las emisiones de carbono
def emission(fuel,consumption):
    fuel_name=df.query("fuel_name==@fuel")['fuel_name']
    heat_content = df.query("fuel_name==@fuel")['heat_content']
    emission_factor = df.query("fuel_name==@fuel")['emission_factor']
    scope = df.query("fuel_name==@fuel")['scope']
    co2=consumption*heat_content*emission_factor
    return fuel_name,scope,co2

#Dataframes para guardar los resultados
df0=[]
df1=[]
df2=[]
df3=[]
consumption_list=[]

#Obtener listado de combustibles
fuels=df['fuel_name']
fuel_list=st.multiselect('Fuel',fuels)

# Filtrar dataframe 
mask_fuels = df['fuel_name'].isin(fuel_list)
df = df[mask_fuels]
#df.drop(['scope','fuel_type','heat_content','unit_heat_content'],axis=1,inplace=True)
st.write(df)

#Obtener listado de consumos
for i in fuel_list:
    consumption=st.number_input(str(i)+" consumption",min_value=1,key=i)
    consumption_list.append(consumption)

#fuel_con=pd.DataFrame(df4)


fuel_name,scope,co2=emission(fuel_list,consumption_list)

df0.append(fuel_name)
df1.append(co2)
df2.append(scope)
#df3.append(fuel_consumption)

fuel_name=pd.DataFrame(df0).transpose().reset_index(drop=True)
fuel_name.columns=['Name']
co2=pd.DataFrame(df1).transpose().reset_index(drop=True)
co2.columns=['CO2 emissions']
scope=pd.DataFrame(df2).transpose().reset_index(drop=True)
scope.columns=['Emissions Scope']

results=pd.concat([fuel_name,co2,scope],axis='columns')

emissions_scope1=results.loc[results['Emissions Scope']==1,'CO2 emissions'].sum()
emissions_scope2=results.loc[results['Emissions Scope']==2,'CO2 emissions'].sum()
emissions_scope3=results.loc[results['Emissions Scope']==3,'CO2 emissions'].sum()

emissions_total=np.sum(results['CO2 emissions'])




#results=pd.concat([fuel_names,fuel_con],axis='columns')

    
if st.button("Results"):
    st.write(results)

 
if st.button('Reset'):
    del results
    



