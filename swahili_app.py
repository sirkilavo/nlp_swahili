import streamlit as st 
from gensim import corpora
import pandas as pd
from gensim.models import LsiModel
import numpy

st.title('Predicting Swahili Headlines')
st.image('image/swahiliprofile.jpg', width = 650)
#st.markdown("'Predicting Swahili Headlines is an AI system which allow someone to write the text and predict a related headline in swahili')
st.markdown("<h4 style='text-align: center; color: ;'>Predicting Swahili Headlines is an AI system which allow someone to write the text and predict a related headline in swahili</h4>", unsafe_allow_html=True)

st.sidebar.title('Tambua Kichwa cha Habari')
with st.sidebar:
    st.markdown("<h4 style='text-align: left; color: green;'>Ingiza Sentensi</h4>", unsafe_allow_html=True)
    sentensi = st.text_input("")

    #sptit text and create dictionary
    sentensi = corpora.Dictionary([sentensi.split()])

    #assign every dictionary to ids, eg 0, 1, 2 
    # st.write(sentensi.token2id)

    #Tokenize the text data
    
    #convert text into numeric number using TIFID
    st.button("Tambua")

   # lsa_model = LsiModel.load("model/lsa_model2")
  
 
  
    
    