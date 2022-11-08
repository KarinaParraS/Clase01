import streamlit as st
st.title('Agua Potable')

col1,col2,col3= st.columns([6,6,6])
x = col1.button(':)')
f = col3.button(':/')
y = col2.button(':c')

st.sidebar.image('https://www.fundacionaquae.org/wp-content/uploads/2020/04/Qu%C3%A9-es-el-agua-3.jpg')
st.sidebar.text('Participantes:')
st.sidebar.text('Vanessa Guerra')
st.sidebar.text('Ashlie Salgueiro')
st.sidebar.text('Karina Parra')
st.sidebar.text('Karol Navarro')
st.sidebar.text('4O Programación')
st.sidebar.text('Facultad de Ciencias Quimicas')
st.sidebar.text('Universidad Autonoma de Chihuahua')
st.sidebar.text('Docente: Jose Manuel Napoles Duarte)
if x:
  st.image('https://static.vecteezy.com/system/resources/previews/001/368/413/non_2x/glass-filled-with-water-and-a-carafe-in-the-background-photo.jpg')
if f:
  st.image('https://img2.freepng.es/20180328/dlw/kisspng-is-the-glass-half-empty-or-half-full-water-shot-g-water-glass-5abbf6afc77e76.5128224415222678238171.jpg')
if y:
  st.image('https://thumbs.dreamstime.com/b/vaso-vac%C3%ADo-de-agua-forma-vino-aislado-en-fondo-blanco-y-negro-vidrio-213224971.jpg')
