import streamlit as st
import numpy as np
import pandas as pd

#Codigo para eliminar el boton de menu y logo de streamlit
#hide_menu_style = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)


st.markdown("# Calculos para varios equipos: por favor, carga el archivo CSV con los consumos de energia de los equipos de tu planta")

file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

df=pd.read_csv("Databases/emission factors demo.csv")
df_equip=pd.read_csv("Databases/equipment list demo.csv")

#Calculo de las emisiones de carbono
@st.cache
def emission(fuel,consumption):
    fuel_name=df.query("fuel_name==@fuel")['fuel_name']
    heat_content = df.query("fuel_name==@fuel")['heat_content']
    emission_factor = df.query("fuel_name==@fuel")['emission_factor']
    fuel_cost = df.query("fuel_name==@fuel")['cost_per_unit']
    scope = df.query("fuel_name==@fuel")['scope']
    co2=consumption*heat_content*emission_factor
    cost=consumption*fuel_cost
    return fuel_name,scope,co2,cost

#Dataframes para guardar los resultados
df0=[]
df1=[]
df2=[]
df3=[]
df4=[]
df5=[]

#Obtener listado de procesos, equipos, combustibles, y consumos
process=df_equip['process_id']
equipment=df_equip['equipment_id']
fuels=df_equip['fuel_name']
consumption=df_equip['consumption']

#Prueba de la funcion
fuel_name,scope,co2,cost=emission(fuels,consumption)

df0.append(fuel_name)
df1.append(co2)
df2.append(scope)
df3.append(cost)
df4.append(process)
df5.append(equipment)

process_name=pd.DataFrame(df4)
process_name.columns=['ID proceso']
equipment_name=pd.DataFrame(df5)
equipment_name.columns=['ID equipo']
fuel_name=pd.DataFrame(df0).transpose().reset_index(drop=True)
fuel_name.columns=['Fuente energia']
co2=pd.DataFrame(df1).transpose().reset_index(drop=True)
co2.columns=['Emisiones kg CO2-eq']
scope=pd.DataFrame(df2).transpose().reset_index(drop=True)
scope.columns=['Alcance emisiones']
cost=pd.DataFrame(df3).transpose().reset_index(drop=True)
cost.columns=['Costo energia USD']

results=pd.concat([process_name,equipment_name,fuel_name,co2,scope,cost],axis='columns')
results.set_index('ID proceso',inplace=True)
st.dataframe(results)


emissions_scope1_fija=results.loc[results['Alcance emisiones']=='1_combustion_fija','Emisiones kg CO2-eq'].sum()
emissions_scope1_movil=results.loc[results['Alcance emisiones']=='1_combustion_movil','Emisiones kg CO2-eq'].sum()
emissions_scope2=results.loc[results['Alcance emisiones']=='2_electricidad','Emisiones kg CO2-eq'].sum()

emissions_total=np.sum(results['Emisiones kg CO2-eq'])
cost_total=np.sum(results['Costo energia USD'])


