import streamlit as st 
import pickle 
import spacy
from spacy import displacy
import os

st.set_page_config("NER")
st.title("Name Entity Recognition")

nlp = spacy.load('en_core_web_lg')

model_load = pickle.load(open('./Pickle_Models/medical_ner', 'rb'))

select_options = ['General NER', 'Medical NER']

selected_option = st.selectbox("Select Any Option", select_options)

if selected_option == 'General NER':  
        text = st.text_input('Enter Text for General NER', value='') 
        doc = nlp(text)
        code = spacy.displacy.render(doc, style='ent')
        st.markdown(code, unsafe_allow_html=True)

elif selected_option == 'Medical NER':
        text = st.text_input('Enter Text for Medical NER', value='')
        doc = model_load(text)
        colors = {'PATHOGEN':"#F67DE3", 'MEDICINE':"#7DF6D9", 'MEDICALCONDITION':"#a6e22d"}
        options= {"colors": colors}
        code = spacy.displacy.render(doc, style='ent', options=options)
        st.markdown(code, unsafe_allow_html=True)


