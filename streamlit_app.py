from collections import namedtuple
import re
import requests
import time
import math
import pandas as pd
import json
import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="EmiGPT",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "mailto:overmars86@gmail.com"
    }
    
)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

image = Image.open("Emicool_Logo.80kb_high_res-removebg-preview.png")
st.image(image)
"""
# Welcome to EmiGPT!

This tool is for Emicool employees only.





"""
promt = ['Fix spelling and grammar:','Paraphrase this:', 'Summarize this:']
def clean_text(text):
    new = str(text)
    new = new.replace("[{'generated_text':", "")
    new = new.replace("[{", "")
    new = new.replace("}]", "")
    new = new.replace("'", "")
    new = new.replace("summary_text:", "")

    return new
# Hagging face API
API_URL_LIST = ["https://api-inference.huggingface.co/models/grammarly/coedit-large",
           "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"]
headers = {"Authorization": "Bearer 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"}



option = st.selectbox(
    'Please select what you want to do',
    ('Fix the grammar', 'Paraphrase' , 'Summarise', 'Draft'))

if option == 'Summarise':
    API_URL	= API_URL_LIST[1]
else: 
     API_URL = API_URL_LIST[0]

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

txt = st.text_area('Enter your text here', '')
st.button("Process the text", type="primary")

if txt:
    with st.spinner('Wait for it...'):
        output = query({"inputs": option +":"+ txt,
                         "options": {"wait_for_model":True},
                         "parameters": {"max_length":500}})
        cln_txt = clean_text(output)
        out_txt = st.text_area("", cln_txt)
