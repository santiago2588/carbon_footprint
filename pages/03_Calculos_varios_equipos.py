import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Codigo para eliminar el boton de menu y logo de streamlit
#hide_menu_style = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)


st.markdown("# Calculos para varios equipos: por favor, carga el archivo CSV con los consumos de energia de los equipos de tu planta")

file_upload = st.file_uploader("Carga el archivo csv", type=["csv"])

if file_upload is not None:

    df_equip=pd.read_csv(file_upload)
    df_equip=df_equip.sort_values('fuel_name')

    df=pd.read_csv("Databases/emission factors demo.csv")


    #Calculo de las emisiones de carbono
    @st.cache
    def emission(fuel,consumption):
        fuel_name=df.query("fuel_name in @fuel")['fuel_name']
        heat_content = df.query("fuel_name in @fuel")['heat_content']
        emission_factor = df.query("fuel_name in @fuel")['emission_factor']
        fuel_cost = df.query("fuel_name in @fuel")['cost_per_unit']
        co2=consumption*heat_content*emission_factor
        scope = df.query("fuel_name in @fuel")['scope']
        cost=consumption*fuel_cost
        return fuel_name,co2,scope,cost

    #Dataframes para guardar los resultados
    df0=[]
    df1=[]
    df2=[]
    df3=[]
    df4=[]
    df5=[]

    #Obtener listado de procesos, equipos, combustibles, y consumos
    process_list=df_equip['process_id'].tolist()
    equipment_list=df_equip['equipment_id'].tolist()
    fuel_list=df_equip['fuel_name'].tolist()
    consumption_list=df_equip['consumption'].tolist()

    #Prueba de la funcion
    fuel_name,co2,scope,cost=emission(fuel_list,consumption_list)

    df0.append(process_list)
    df1.append(equipment_list)
    df2.append(fuel_name)
    df3.append(co2)
    df4.append(scope)
    df5.append(cost)

    process_name=pd.DataFrame(df0).transpose().reset_index(drop=True)
    process_name.columns=['ID proceso']
    equipment_name=pd.DataFrame(df1).transpose().reset_index(drop=True)
    equipment_name.columns=['ID equipo']
    fuel_name=pd.DataFrame(df2).transpose().reset_index(drop=True)
    fuel_name.columns=['Fuente energia']
    co2=pd.DataFrame(df3).transpose().reset_index(drop=True)
    co2.columns=['Emisiones kg CO2-eq']
    scope=pd.DataFrame(df4).transpose().reset_index(drop=True)
    scope.columns=['Alcance emisiones']
    cost=pd.DataFrame(df5).transpose().reset_index(drop=True)
    cost.columns=['Costo energia USD']


    results=pd.concat([process_name,equipment_name,fuel_name,co2,scope,cost],axis='columns')
    #results.set_index('ID proceso',inplace=True)
    st.dataframe(results)

    emissions_total=np.sum(results['Emisiones kg CO2-eq'])
    cost_total=np.sum(results['Costo energia USD'])

    col1,col2=st.columns(2)

    with col1:
        st.metric('Total emisiones de carbono',str("%.1f" % np.float_(emissions_total))+ ' kg CO2-eq')

    with col2:
        st.metric('Costo total de energia',str("%.1f" % np.float_(cost_total))+ ' USD')

    with st.expander('Contribucion fuentes de energia'):
        fig_results = px.pie(results, names='Fuente energia', values='Emisiones kg CO2-eq', hover_data=['Costo energia USD'])
        st.plotly_chart(fig_results, use_container_width=True)

    with st.expander('Contribucion procesos'):
        fig_process = px.pie(results, names='ID proceso', values='Emisiones kg CO2-eq', hover_data=['Costo energia USD'])
        st.plotly_chart(fig_process, use_container_width=True)

    with st.expander('Contribucion equipos'):
        fig_equipment = px.pie(results, names='ID equipo', values='Emisiones kg CO2-eq', hover_data=['Costo energia USD'])
        st.plotly_chart(fig_equipment, use_container_width=True)