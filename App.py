%%writefile app.py
import streamlit as st

st.title("AGUA POTABLE")

col1,col2 = st.columns([6,6])

a = st.sidebar.button('¿Como Funciona un filtro?')
b = st.sidebar.button('Tipos de Filtros')

if col2.button("Filtro de Carbon Activado"):
  st.write("Elimina:")
  st.write("Años de vida del filtro: se recomienda cambiar el carbón activado cada año")
  st.write("Efectividad: Los filtros de carbón activado de calidad pueden eliminar el 95 % o más del cloro libre.")
  st.image("https://www.aquaprof.es/wp/wp-content/uploads/2017/11/filtro-cabon-funcionamiento.jpg")

d = col3,col4,col5 = st.columns([7,7,7])
if col3.button("Filtro Doble"):
  st.write("Elimina: Turbidez, Polvos orgánicos, Olor y sabor a cloro.")
  st.write("Años de vida del filtro: la vida de este filtro es de aproximadamente 6 meses")
  st.image("https://m.media-amazon.com/images/I/61GmdwHVkeL._AC_SX425_.jpg")

if col4.button("Filtros Triple"):
  st.write("Elimina: Microorganismos:cteoliformes, salmonela, fecales, totales, etc., Turbidez, Polvos orgánicos, Olor y sabor a cloro.")
  st.write("Años de vida del filtro: Se aproxima que la vida del filtro .")
  
  st.image("https://m.media-amazon.com/images/I/71Vn5M1CV1L._AC_UF894,1000_QL80_.jpg")

if col5.button("Osmosis"):
  st.write("Elimina: Iones y metales, Microorganismos, Turbidez, Polvos Orgánicos, Olor y sabor a cloro.")
  st.write("Años de vida del filtro: Se aproxima que la vida del filtro .")
  st.image("https://www.homea.mx/Files/119914/Img/05/FILTRO-DE-AGUA-OSMOSIS-INVERSA-WHIRLPOOL-WK3901Q-zoom.jpg")

if col1.button("Filtro de Osmosis Inversa"):
  st.write("Elimina:")
  st.write("Años de vida del filtro: En equipos de calidad y bien calibrados en su diseño, la duración de la membrana viene a ser de entre 3 a 5 años. Es importante hacer los mantenimientos periódicos, siguiendo los consejos del fabricante.")
  st.write("Efectividad: La ósmosis inversa es capaz de eliminar hasta el 99% de las sales disueltas (iones), partículas, coloides, orgánicos, bacterias y pirógenos del agua con que se alimenta el sistema (aunque no se debe confiar en un sistema de ósmosis inversa para eliminar el 100% de las bacterias y virus).")
  st.image("https://www.iagua.es/sites/default/files/images/medium/osmosisinversa-ro-5.jpg")



st.sidebar.image('https://www.fundacionaquae.org/wp-content/uploads/2020/04/Qu%C3%A9-es-el-agua-3.jpg')
st.sidebar.caption('Participantes:')
st.sidebar.caption('Vanessa Guerra')
st.sidebar.caption('Ashlie Salgueiro')
st.sidebar.caption('Karina Parra')
st.sidebar.caption('Karol Navarro')
st.sidebar.caption('4O Programación')
st.sidebar.caption('Facultad de Ciencias Quimicas')
st.sidebar.caption('Universidad Autonoma de Chihuahua')
st.sidebar.caption('Docente: Jose Manuel Napoles Duarte')
