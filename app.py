import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()
st.markdown("<h1 style='text-align: center; color: #2a3a65;'>Textblob mide tus emociones</h1>", unsafe_allow_html=True)

st.subheader("Escribe la frase que deseas analizar:")
st.write("Escribe una palabra que sea un sentimiento.")
with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
               **Una breve guía de los parámetros:**
                
                **Polaridad:** _Este dira si el texto puesto es positivo, negativo o neutral. 
                Si el valor esta entre -1 (muy negativo) y 1 (muy positivo), con 0 un sentimiento neutral._
                
               **Subjetividad:** _Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo._

                 """
               ) 


with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe aqui: ')
    if text1:

        #translation = translator.translate(text1, src="es", dest="en")
        #trans_text = translation.text
        #blob = TextBlob(trans_text)
        blob = TextBlob(text1)
       
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
            st.image('Feli.jpg', width=300)  # Imagen positiva
            st.audio('happy.mp3')  # Sonido para sentimiento positivo
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
            st.image('sad.jpg', width=300)  
            st.audio('miau.mp3')  
        else:
            st.write( 'Es un sentimiento Neutral 😐')
            st.image('neutral.jpg', width=300)  # Imagen positiva
            st.audio('huh.mp3')  # Sonido para sentimiento positivo

with st.expander('Corrección en inglés'):
       text2 = st.text_area('Escribe por favor: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct())) 
