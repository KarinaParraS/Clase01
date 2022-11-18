import streamlit as st

st.title("AGUA POTABLE")

col1,col2 = st.columns([10,10])

st.header('Diferencia entre el Agua de grifo y el Agua pura')
st.write('El agua que obtenemos del grifo es considerada por organismos internacionales como potable. Sin embargo, que sea apta para consumo no quiere decir que sea agua pura, y este es el error que cometen muchas personas. El agua de grifo, aunque ha pasado por tratamientos previos para descontaminarla, recolecta otro tipo de impurezas en el camino')
st.sidebar.button('Tipos de Filtros')

if col2.button("Filtro de Carbon Activado"):
  st.write("Años de vida del filtro: ¡Un filtro puede llegar a durar hasta 10 años sin ningún tipo de problema con un cuidado adecuado! Y es que, además, el mantenimiento del filtro de carbón activo es tremendamente sencillo. Para limpiarlo solo necesitarás meterlo en el horno a una temperatura de 200 ºC")
  st.write("Efectividad: pueden atrapar el 99.97% de las partículas pequeñas de 0.3 micrones o más grandes, así como la mayoría de las partículas más grandes, especialmente las esporas.")
  st.write("Daños a la salud: Ciertos contaminantes no se eliminarán al usar un filtro de agua de carbón. Estos contaminantes incluyen minerales tóxicos, fluoruros, nitratos y una variedad de microorganismos que son dañinos para la salud")
  st.image("https://www.aquaprof.es/wp/wp-content/uploads/2017/11/filtro-cabon-funcionamiento.jpg")

d = col3,col4 = st.columns([7,7])
if col3.button("Filtro Doble"):
  st.write("Años de vida del filtro: La vida media del filtro es de 6 meses")
  st.write("Efectividad: Este filtro puede eliminar partirlas de Sal hasta un 95% ")
  st.write("Daños a la salud: Como cualquier otro filtro si no se le da un buen mantenimiento o se cambia adecuadamente puede generar bacterias y eso es dañino para nuestra salud.")
  st.image("https://m.media-amazon.com/images/I/61GmdwHVkeL._AC_SX425_.jpg")

if col4.button("Filtros Triple"):
  st.write("Años de vida: tienen un periodo de vida bastante extendido, incluso puede llegar a durar algunas décadas, pero el cartucho interno que es el que hace todo el trabajo de purificación, sí que tiene un periodo de vida más limitado de aproximadamente 1 año.")

st.write("Efectividad: El filtro triple filtrado tecnología de vanguardia usada en diálisis para desinfectar con eficiencia el 100% de microbios ya sean bacterias (0.2 a 2 micras de tamaño) parásitos, protozoarios, quistes de amibas. ")

st.write("Daños a la salud: Si el filtro no se controla puede empezar a crecer moho, sobre todo en un lugar húmedo. No sólo el agua tendrá mal sabor, sino que lo ingerirás. La ingestión puede causar dolores de cabeza, secreción nasal, sinusitis, exantema, diarrea y posibles vómitos.")
  st.image("https://m.media-amazon.com/images/I/71Vn5M1CV1L._AC_UF894,1000_QL80_.jpg")


if col1.button("Filtro de Osmosis Inversa"):
  st.write("Años de vida del filtro: En equipos de calidad y bien calibrados en su diseño, la duración de la membrana viene a ser de entre 3 a 5 años. Es importante hacer los mantenimientos periódicos, siguiendo los consejos del fabricante.")
  st.write("Efectividad: es capaz de eliminar hasta el 99% de las sales disueltas (iones)")
  st.write("Daños a la salud: Una de las principales razones por las que no se recomienda beber agua purificada mediante ósmosis inversa es porque la eliminación de los minerales hace que el agua se vuelva ácida (a menudo muy por debajo de 7.0 pH). Beber agua ácida no ayuda a mantener un equilibrio saludable de pH en la sangre")
  st.image("https://www.homea.mx/Files/119914/Img/05/FILTRO-DE-AGUA-OSMOSIS-INVERSA-WHIRLPOOL-WK3901Q-zoom.jpg")
  st.image("https://www.iagua.es/sites/default/files/images/medium/osmosisinversa-ro-5.jpg")

st.header('Huella hídrica')

col6, col7 = st.columns([6,6])

if col6.button('¿Como se define una huella Hidrica?'):
  st.write("Es un indicador de toda el agua que utilizamos en nuestra vida diaria; para producir nuestra comida, en procesos industriales y generación de energía, así como la que ensuciamos y contaminamos a través de esos mismos procesos.")
  st.write("Nos permite conocer la cantidad de agua que aprovecha una persona, un grupo de consumidores, una región, país o toda la humanidad.")
  st.image('https://sites.google.com/site/lahuellahidrica/_/rsrc/1432694053802/la-huella-hidrica-en-mexico/Imagen1.jpg')

if col7.button('La importancia de la huella hidrica'):
  st.write("Los hábitos alimenticios, patrones de consumo y estilo de vida como el transporte, tecnología, aficiones son factores que determinan la magnitud de nuestra huella hídrica individual. Hay que considerar que, invariablemente, la cantidad de agua que se utilizó en un proceso fue a costa de otro posible uso, o del agua que requieren los ecosistemas.")
  st.write("Nuestras decisiones cotidianas, aparentemente tan chiquitas e inocentes en el contexto nacional o global, tienen efectos multiplicativos, para bien o para mal. Un patrón responsable de consumo puede contribuir, litro a litro, a aminorar la competencia sobre los cada vez más escasos recursos hídricos.")
  st.image('https://1.bp.blogspot.com/-S7AtxDCxUko/YQL7geNvU3I/AAAAAAAAEaU/ejX2N9jUP6ooyrWJnGj-uKbuzBlKO2PMACLcBGAsYHQ/w1200-h630-p-k-no-nu/Imagen3.jpg')


st.sidebar.image('https://www.fundacionaquae.org/wp-content/uploads/2020/04/Qu%C3%A9-es-el-agua-3.jpg')

st.sidebar.caption('Desarolladores:')
st.sidebar.caption('Karina Parra')
st.sidebar.caption('Vanessa Guerra')
st.sidebar.caption('Ashlie Salgueiro')
st.sidebar.caption('Karol Navarro')
st.sidebar.caption('4O Programación')
st.sidebar.caption('Facultad de Ciencias Químicas')
st.sidebar.caption('Universidad Autónoma de Chihuahua')
st.sidebar.caption('Docente: Jose Manuel Napoles Duarte')
