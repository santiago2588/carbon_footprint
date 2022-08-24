# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:19:54 2022

@author: mjkipsz2
"""

import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

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

st.subheader('1. Selecciona las fuentes de energia que utilizas en tu planta')

#Obtener listado de combustibles
fuels=df['fuel_name']
fuel_list=st.multiselect('Fuentes de energia',fuels)

# Filtrar dataframe 
mask_fuels = df['fuel_name'].isin(fuel_list)
df = df[mask_fuels]
st.write(df)

st.subheader('2. Ingresa los consumos de las fuentes de energia que seleccionaste, en las unidades correspondientes que se muestran en la tabla anterior')

#Obtener listado de consumos
for i in fuel_list:
    consumption=st.number_input(str(i)+" consumption",min_value=1,key=i)
    consumption_list.append(consumption)

#Prueba de la funcion
fuel_name,scope,co2=emission(fuel_list,consumption_list)

df0.append(fuel_name)
df1.append(co2)
df2.append(scope)

fuel_name=pd.DataFrame(df0).transpose().reset_index(drop=True)
fuel_name.columns=['Name']
co2=pd.DataFrame(df1).transpose().reset_index(drop=True)
co2.columns=['CO2 emissions']
scope=pd.DataFrame(df2).transpose().reset_index(drop=True)
scope.columns=['Emissions Scope']

results=pd.concat([fuel_name,co2,scope],axis='columns')

emissions_scope1_fija=results.loc[results['Emissions Scope']=='1_combustion_fija','CO2 emissions'].sum()
emissions_scope1_movil=results.loc[results['Emissions Scope']=='1_combustion_movil','CO2 emissions'].sum()
emissions_scope2=results.loc[results['Emissions Scope']=='2_electricidad','CO2 emissions'].sum()

emissions_total=np.sum(results['CO2 emissions'])

st.subheader('3. Presiona el boton Resultados para obtener las emisiones de carbono de tu planta')

if st.button("Resultados"):
    st.write(results)
    st.metric('Total emisiones',str("%.1f" % np.float_(emissions_total))+ ' CO2-eq')
    
    col1,col2,col3=st.columns(3)
        
    with col1:
        st.metric('Emisiones Alcance 1-Combustion fija',str("%.1f" % np.float_(emissions_scope1_fija))+' CO2-eq')
            
    with col2:
        st.metric('Emisiones Alcance 1-Combustion movil',str("%.1f" % np.float_(emissions_scope1_movil))+' CO2-eq')
            
    with col3:
        st.metric('Emisiones Alcance 2',str("%.1f" % np.float_(emissions_scope2))+' CO2-eq')
        
        
if st.button('Beneficios'): 
        st.success("Felicitaciones, has comenzado a desbloquear algunos de los beneficios de la digitalización y el procesamiento de datos con modelos cientificos e inteligencia artificial.") 
        st.markdown("En esta ocasion, te hemos presentado los beneficios del modulo de Calculos. Sin embargo, quedan inmensas oportunidades para optimizar la productividad y el desempeño de los pozos petroleros al integrar todos los modulos de ASTRO") 
        st.markdown("Si estás listo para emprender este camino y llevar la digitalización al siguiente nivel, contactate con nosotros para guiarte en el proceso y recibir asesoria de nuestros expertos para optimizar tus operaciones.")
    
        contact_form = """
        <form action="https://formsubmit.co/zapaz.consultores@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="Nombre" placeholder="Tu nombre" required>
             <input type="email" name="email" placeholder="Tu email" required>
             <textarea name="message" placeholder="Tu mensaje"></textarea>
             <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style.css")



