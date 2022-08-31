import streamlit as st

st.markdown("# Instrucciones")

with st.expander("Qué es la huella de carbono y cómo se calcula?"):
    
    st.markdown("La huella de carbono representa las emisiones de los gases de efecto invernadero debido al consumo de combustibles de origen fósil,\
                (por ejemplo, la gasolina o fuel oil) y al consumo de electricidad en las operaciones industriales.")
    
    st.markdown(
        """
        De acuerdo con estándares internacionales, se distinguen dos tipos de alcances para el cálculo de la huella de carbono. 
        - El primer alcance se relaciona con las emisiones por la combustión de combustibles en fuentes fijas (por ejemplo, calderos) o móviles (por ejemplo, vehículos). 
        - El segundo alcance se relaciona con las emisiones por el consumo de electricidad en las operaciones (por ejemplo, para operar un equipo industrial).
                 """
                )
    
    #image1 = Image.open('modulos ASTRO.png')
    #st.image(image1)
    

with st.expander('Instrucciones'):
    
    st.markdown("""
    ### AUCAF es una herramienta digital que permite calcular la huella de carbono en las operaciones industriales, y los costos de energía asociados""")
    
    st.markdown("AUCAF es una solucion modular que se adapta a tus necesidades y genera valor en tus operaciones. AUCAF incluye los siguientes modulos:")
    
    #image1 = Image.open('modulos ASTRO.png')
    #st.image(image1)
      
    st.markdown('En esta demostracion, te presentamos el Modulo de Calculos, que permite calcular tus emisiones de carbono y costos de energia en tus operaciones.')
                 
    st.markdown('Esta herramienta tambien permite reducir tus emisiones de carbono y costos de energia en funcion de los resultados obtenidos en el modelo\
                  generando beneficios economicos. Para ello, la herramienta utiliza predicciones basadas en inteligencia artificial y metodologias para la integracion de procesos y eficiencia energetica.')
