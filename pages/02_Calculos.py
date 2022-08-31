import streamlit as st
import numpy as np
import pandas as pd

st.markdown("# Calculos")
st.write('Por favor, sigue los pasos que se presentan a continuacion.')

df=pd.read_csv('emission factors demo.csv')

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

with st.expander('1. Selecciona las fuentes de energia que utilizas en tu planta y los consumos en las unidades correspondientes que se muestran en la tabla'):
    
    #Obtener listado de combustibles
    fuels=df['fuel_name']
    fuel_list=st.multiselect('Fuentes de energia',fuels)

    # Filtrar dataframe 
    mask_fuels = df['fuel_name'].isin(fuel_list)
    df = df[mask_fuels]
    st.dataframe(df)

   
    #Obtener listado de consumos
    for i in fuel_list:
        consumption=st.number_input("CONSUMO "+ str(i),min_value=1,key=i)
        consumption_list.append(consumption)

    #Prueba de la funcion
    fuel_name,scope,co2,cost=emission(fuel_list,consumption_list)

    df0.append(fuel_name)
    df1.append(co2)
    df2.append(scope)
    df3.append(cost)

    fuel_name=pd.DataFrame(df0).transpose().reset_index(drop=True)
    fuel_name.columns=['Name']
    co2=pd.DataFrame(df1).transpose().reset_index(drop=True)
    co2.columns=['CO2 emissions']
    scope=pd.DataFrame(df2).transpose().reset_index(drop=True)
    scope.columns=['Emissions Scope']
    cost=pd.DataFrame(df3).transpose().reset_index(drop=True)
    cost.columns=['Fuel cost USD']

    results=pd.concat([fuel_name,co2,scope,cost],axis='columns')

    emissions_scope1_fija=results.loc[results['Emissions Scope']=='1_combustion_fija','CO2 emissions'].sum()
    emissions_scope1_movil=results.loc[results['Emissions Scope']=='1_combustion_movil','CO2 emissions'].sum()
    emissions_scope2=results.loc[results['Emissions Scope']=='2_electricidad','CO2 emissions'].sum()

    emissions_total=np.sum(results['CO2 emissions'])
    cost_total=np.sum(results['Fuel cost USD'])

with st.expander('2. Visualiza las emisiones de carbono de tu planta y los costos de energia'):

    st.dataframe(results)

    st.success('Resultados de tus emisiones de carbono')

    st.metric('Total emisiones',str("%.1f" % np.float_(emissions_total))+ ' CO2-eq')

    col1,col2,col3=st.columns(3)

    with col1:
        st.metric('Emisiones Alcance 1-Combustion fija',str("%.1f" % np.float_(emissions_scope1_fija))+' CO2-eq')

    with col2:
        st.metric('Emisiones Alcance 1-Combustion movil',str("%.1f" % np.float_(emissions_scope1_movil))+' CO2-eq')

    with col3:
        st.metric('Emisiones Alcance 2',str("%.1f" % np.float_(emissions_scope2))+' CO2-eq')

    st.success('Resultados de tus costos energeticos')

    st.metric('Costo total de energia',str("%.1f" % np.float_(cost_total))+ ' USD')
        

with st.expander("3. Descubre cuanto podrias disminuir tus emisiones de carbono y tus costos de energia con nuestra tecnologia"):      

    co2_reduced=emissions_total*0.2
    co2_new=emissions_total*0.8

    col1,col2=st.columns(2)

    with col1:
        st.metric('Emisiones que se pueden reducir',str("%.1f" % np.float_(co2_reduced))+ ' CO2-eq')

    with col2:
        st.metric('Tus nuevas emisiones de carbono son',str("%.1f" % np.float_(co2_new))+ ' CO2-eq')

    
    cost_reduced=cost_total*0.2
    cost_new=cost_total*0.8

    col1,col2=st.columns(2)

    with col1:
        st.metric('Costos de energia que se pueden reducir',str("%.1f" % np.float_(cost_reduced))+ ' USD')

    with col2:
        st.metric('Tus nuevos costos de energia son',str("%.1f" % np.float_(cost_new))+ ' USD')

    st.success('Felicitaciones, has reducido tus emisiones de carbono y los costos energeticos y ahora tu planta es mas rentable y eficiente!')
