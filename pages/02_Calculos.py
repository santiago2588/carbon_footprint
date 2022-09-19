import streamlit as st
import numpy as np
import pandas as pd

#Codigo para eliminar el boton de menu y logo de streamlit
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.markdown("# Calculos")
st.write('Por favor, sigue los pasos que se presentan a continuacion.')

df=pd.read_csv("Databases/emission factors demo.csv")

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
consumption_list=[]

with st.expander('1. Selecciona las fuentes de energia que utilizas en tu planta e ingresa los consumos en las unidades correspondientes'):
    
    #Obtener listado de combustibles
    fuels=df['fuel_name']
    fuel_list=st.multiselect('Fuentes de energia',fuels)

    # Filtrar dataframe 
    mask_fuels = df['fuel_name'].isin(fuel_list)
    df = df[mask_fuels]
    fuel_data=df[['fuel_name','consumption_unit','cost_per_unit']]
    fuel_data=fuel_data.rename(columns={'fuel_name':'Fuente de energia','consumption_unit':'Unidad consumo de energia','cost_per_unit':'Costo USD por unidad de energia '})
    #st.dataframe(fuel_data)

   
    #Obtener listado de consumos
    for i in fuel_list:
        fuel_unit=df.query("fuel_name==@i")['consumption_unit'].to_string(index=False)
        consumption=st.number_input("Consumo "+ str(i)+" en "+fuel_unit,key=i)
        consumption_list.append(consumption)

    #Prueba de la funcion
    fuel_name,scope,co2,cost=emission(fuel_list,consumption_list)

    df0.append(fuel_name)
    df1.append(co2)
    df2.append(scope)
    df3.append(cost)

    fuel_name=pd.DataFrame(df0).transpose().reset_index(drop=True)
    fuel_name.columns=['Fuente energia']
    co2=pd.DataFrame(df1).transpose().reset_index(drop=True)
    co2.columns=['Emisiones kg CO2-eq']
    scope=pd.DataFrame(df2).transpose().reset_index(drop=True)
    scope.columns=['Alcance emisiones']
    cost=pd.DataFrame(df3).transpose().reset_index(drop=True)
    cost.columns=['Costo energia USD']

    results=pd.concat([fuel_name,co2,scope,cost],axis='columns')
    results=pd.DataFrame(results).reset_index(drop=True)

    emissions_scope1_fija=results.loc[results['Alcance emisiones']=='1_combustion_fija','Emisiones kg CO2-eq'].sum()
    emissions_scope1_movil=results.loc[results['Alcance emisiones']=='1_combustion_movil','Emisiones kg CO2-eq'].sum()
    emissions_scope2=results.loc[results['Alcance emisiones']=='2_electricidad','Emisiones kg CO2-eq'].sum()

    emissions_total=np.sum(results['Emisiones kg CO2-eq'])
    cost_total=np.sum(results['Costo energia USD'])

with st.expander('2. Calcula las emisiones de carbono de tu planta y los costos de energia'):

    col1,col2=st.columns(2)

    with col1:
        st.metric('Total emisiones de carbono',str("%.1f" % np.float_(emissions_total))+ ' kg CO2-eq')

    #col1,col2,col3=st.columns(3)

    #with col1:
        #st.metric('Emisiones Alcance 1-Combustion fija',str("%.1f" % np.float_(emissions_scope1_fija))+' kg CO2-eq')

    #with col2:
        #st.metric('Emisiones Alcance 1-Combustion movil',str("%.1f" % np.float_(emissions_scope1_movil))+' kg CO2-eq')

    #with col3:
        #st.metric('Emisiones Alcance 2',str("%.1f" % np.float_(emissions_scope2))+' kg CO2-eq')

    with col2:
        st.metric('Costo total de energia',str("%.1f" % np.float_(cost_total))+ ' USD')

    if st.button('Ver detalle'):
        st.dataframe(results)

with st.expander("3. Descubre cuanto podrias disminuir tus emisiones de carbono y tus costos de energia con nuestra tecnologia"):      

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

    st.success("""
    Felicitaciones, has reducido tus emisiones de carbono y los costos energeticos y ahora tu planta es mas rentable y eficiente! 
    
    En esta ocasion, te hemos presentado los beneficios del modulo de Calculos. Sin embargo, quedan inmensas oportunidades para disminuir tu huella de carbono al integrar todos los modulos de AUCAF.
    
    Si quieres conocer como puedes lograr estos beneficios, contáctanos para guiarte en el proceso y recibir asesoria de nuestros expertos.""")
