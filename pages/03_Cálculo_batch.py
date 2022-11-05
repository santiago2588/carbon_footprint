import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#Codigo para eliminar el boton de menu y logo de streamlit
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.markdown("# Calculo batch")

st.markdown("Carga el archivo CSV con los consumos de energia de las areas y equipos de tu planta")

file_upload = st.file_uploader("", type=["csv"])

if file_upload is not None:

    df_equip=pd.read_csv(file_upload)
    df_equip=df_equip.sort_values('fuel_name')

    st.markdown("## Tabla de datos")
    st.dataframe(df_equip)

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

    with st.expander("Resultados"):

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

    with st.expander('Contribucion emisiones de carbono'):

        tab1, tab2, tab3 = st.tabs(["Fuentes de energia", "Equipos", "Procesos"])

        with tab1:
            fig_results = px.pie(results, names='Fuente energia', values='Emisiones kg CO2-eq', hole=0.4,hover_data=['Costo energia USD'])
            st.plotly_chart(fig_results, use_container_width=True)

        with tab2:
            fig_equipment = px.pie(results, names='ID equipo', values='Emisiones kg CO2-eq', hole=0.4, hover_data=['Costo energia USD'])
            st.plotly_chart(fig_equipment, use_container_width=True)

        with tab3:
            fig_process = px.pie(results, names='ID proceso', values='Emisiones kg CO2-eq', hole=0.4, hover_data=['Costo energia USD'])
            st.plotly_chart(fig_process, use_container_width=True)

    with st.expander("Descubre cuánto podrías disminuir tus emisiones de carbono y tus costos de energía con AUCAF"):

        co2_reduced=emissions_total*0.1
        co2_new=emissions_total*0.9

        #Se asume que un árbol almacena unos 167 kg de CO2 al año https://climate.selectra.com/es/actualidad/co2-arbol
        arboles=co2_reduced/167

        col1,col2=st.columns(2)

        with col1:
            st.metric('Emisiones que se pueden reducir',str("%.1f" % np.float_(co2_reduced))+ ' kg CO2-eq')

        with col2:
            st.metric('Tus nuevas emisiones de carbono son',str("%.1f" % np.float_(co2_new))+ ' kg CO2-eq')

        st.write('Tu reduccion de emisiones equivalen a que siembres',str("%.1f" % np.float_(arboles))+ ' arboles 🌳')

        cost_reduced=cost_total*0.1
        cost_new=cost_total*0.9

        col1,col2=st.columns(2)

        with col1:
            st.metric('Costos de energia que se pueden reducir',str("%.1f" % np.float_(cost_reduced))+ ' USD')

        with col2:
            st.metric('Tus nuevos costos de energia son',str("%.1f" % np.float_(cost_new))+ ' USD')

        st.success("Felicitaciones, has reducido tus emisiones de carbono y los costos energeticos y ahora tu planta es mas rentable y eficiente!")