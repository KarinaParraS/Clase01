import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://gifimage.net/wp-content/uploads/2017/09/animated-water-gif-10.gif");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True)
add_bg_from_url() 
st.title("Purificación del Agua")
st.write('El consumo de agua de mala calidad o agua contaminada, ocasiona enfermedades gastrointestinales, diarreas agudas y otras enfermedades que podrían incluso terminar en una tifoidea o hepatitis, esa es la principal importancia del agua potable. El 70% del planeta Tierra es agua, se calcula que del total de esa agua, el 97% es agua salada, y el 2.5% es considerada dulce. Sin embargo, el 90% de agua dulce se encuentra en la Antártida, y solo el 0.5% de agua dulce se encuentra en los depósitos subterráneos y el 0.01% en ríos y lagos.')
st.subheader('Diferencia entre el Agua de grifo y el Agua pura')
st.write('El agua que obtenemos del grifo es considerada por organismos internacionales como potable. Sin embargo, que sea apta para consumo no quiere decir que sea agua pura, y este es el error que cometen muchas personas. El agua de grifo, aunque ha pasado por tratamientos previos para descontaminarla, recolecta otro tipo de impurezas en el camino')

col1,col2 = st.columns([10,10])

st.sidebar.button('Tipos de Filtros')

if col2.button("Filtro de Carbon Activado"):
  st.subheader('Años de vida del filtro:')
  st.write("Un filtro puede llegar a durar hasta 10 años sin ningún tipo de problema con un cuidado adecuado, Y es que, además, el mantenimiento del filtro de carbón activo es tremendamente sencillo. Para limpiarlo solo necesitarás meterlo en el horno a una temperatura de 200 ºC")
  st.subheader('Efectividad:')
  st.write("Pueden atrapar el 99.97% de las partículas pequeñas de 0.3 micrones o más grandes, así como la mayoría de las partículas más grandes, especialmente las esporas.")
  st.subheader('Daños a la salud:')
  st.write("Ciertos contaminantes no se eliminarán al usar un filtro de agua de carbón. Estos contaminantes incluyen minerales tóxicos, fluoruros, nitratos y una variedad de microorganismos que son dañinos para la salud")
  st.subheader('¿Como funciona?:')
  st.write('Uno de los métodos más populares en los hogares es el filtro de carbón activado. Este sistema se utiliza en distintos niveles, desde casas hasta grandes industrias. La razón de su popularidad es que el carbón, una vez sometido a altas temperaturas, se compacta y se generan pequeños agujeros, tan microscópicos que pueden retener hasta virus y bacterias que son invisibles a la vista.')
  st.image("https://www.aquaprof.es/wp/wp-content/uploads/2017/11/filtro-cabon-funcionamiento.jpg")

d = col3,col4 = st.columns([7,7])
if col3.button("Filtro Doble"):
  st.subheader('Años de vida del filtro:')
  st.write("La vida media del filtro es de 6 meses")
  st.subheader('Efectividad:')
  st.write("Este filtro puede eliminar partirlas de Sal hasta un 95% ")
  st.subheader('Daños a la salud:')
  st.write("Como cualquier otro filtro si no se le da un buen mantenimiento o se cambia adecuadamente puede generar bacterias y eso es dañino para nuestra salud.")
  st.image("https://m.media-amazon.com/images/I/61GmdwHVkeL._AC_SX425_.jpg")

if col4.button("Filtros Triple"):
  st.subheader('Años de vida del filtro:')
  st.write("Años de vida: tienen un periodo de vida bastante extendido, incluso puede llegar a durar algunas décadas, pero el cartucho interno que es el que hace todo el trabajo de purificación, sí que tiene un periodo de vida más limitado de aproximadamente 1 año.")
  st.subheader('Efectividad:')
  st.write("El filtro triple filtrado tecnología de vanguardia usada en diálisis para desinfectar con eficiencia el 100% de microbios ya sean bacterias (0.2 a 2 micras de tamaño) parásitos, protozoarios, quistes de amibas. ")
  st.subheader('Daños a la salud:')
  st.write("Si el filtro no se controla puede empezar a crecer moho, sobre todo en un lugar húmedo. No sólo el agua tendrá mal sabor, sino que lo ingerirás. La ingestión puede causar dolores de cabeza, secreción nasal, sinusitis, exantema, diarrea y posibles vómitos.")
  st.image("https://m.media-amazon.com/images/I/71Vn5M1CV1L._AC_UF894,1000_QL80_.jpg")


if col1.button("Filtro de Osmosis Inversa"):
  st.subheader('Años de vida del filtro:')
  st.write("En equipos de calidad y bien calibrados en su diseño, la duración de la membrana viene a ser de entre 3 a 5 años. Es importante hacer los mantenimientos periódicos, siguiendo los consejos del fabricante.")
  st.subheader('Efectividad:')
  st.write("Es capaz de eliminar hasta el 99% de las sales disueltas (iones)")
  st.subheader('Daños a la salud:')
  st.write("Una de las principales razones por las que no se recomienda beber agua purificada mediante ósmosis inversa es porque la eliminación de los minerales hace que el agua se vuelva ácida (a menudo muy por debajo de 7.0 pH). Beber agua ácida no ayuda a mantener un equilibrio saludable de pH en la sangre")
  st.subheader('¿Como funciona?:')
  st.write('El filtro por ósmosis inversa es un dispositivo que tiene un funcionamiento muy sencillo y resulta altamente eficaz. Consiste en pasar el agua con fuerza a través de una membrana semipermeable muy fina. Esta tiene la capacidad de retener cualquier impureza inorgánica, partículas y sustancias contaminantes como iones de calcio y magnesio que se encuentre en el agua y la endurecen. La membrana retiene los restos y solo logra traspasar el agua pura.') 
  st.image("https://www.iagua.es/sites/default/files/images/medium/osmosisinversa-ro-5.jpg")

st.subheader('Huella hídrica')

col6, col7 = st.columns([6,6])

if col6.button('¿Como se define una huella Hidrica?'):
  st.write("Es un indicador de toda el agua que utilizamos en nuestra vida diaria; para producir nuestra comida, en procesos industriales y generación de energía, así como la que ensuciamos y contaminamos a través de esos mismos procesos.")
  st.write("Nos permite conocer la cantidad de agua que aprovecha una persona, un grupo de consumidores, una región, país o toda la humanidad.")
  st.image('https://sites.google.com/site/lahuellahidrica/_/rsrc/1432694053802/la-huella-hidrica-en-mexico/Imagen1.jpg')

if col7.button('La importancia de la huella hidrica'):
  st.write("Los hábitos alimenticios, patrones de consumo y estilo de vida como el transporte, tecnología, aficiones son factores que determinan la magnitud de nuestra huella hídrica individual. Hay que considerar que, invariablemente, la cantidad de agua que se utilizó en un proceso fue a costa de otro posible uso, o del agua que requieren los ecosistemas.")
  st.write("Nuestras decisiones cotidianas, aparentemente tan chiquitas e inocentes en el contexto nacional o global, tienen efectos multiplicativos, para bien o para mal. Un patrón responsable de consumo puede contribuir, litro a litro, a aminorar la competencia sobre los cada vez más escasos recursos hídricos.")
  st.image('https://1.bp.blogspot.com/-S7AtxDCxUko/YQL7geNvU3I/AAAAAAAAEaU/ejX2N9jUP6ooyrWJnGj-uKbuzBlKO2PMACLcBGAsYHQ/w1200-h630-p-k-no-nu/Imagen3.jpg')

import pandas as pd
import numpy as np

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

st.sidebar.image('https://rotoplas.com.mx/rtp-resources/categorias/rotoplas_mx_soluciones_purificacion.png')

st.sidebar.caption('Desarolladores:')
st.sidebar.caption('Karina Parra')
st.sidebar.caption('Vanessa Guerra')
st.sidebar.caption('Ashlie Salgueiro')
st.sidebar.caption('Karol Navarro')
st.sidebar.caption('4O Programación')
st.sidebar.caption('Facultad de Ciencias Químicas')
st.sidebar.caption('Universidad Autónoma de Chihuahua')
st.sidebar.caption('Docente: Jose Manuel Napoles Duarte')
