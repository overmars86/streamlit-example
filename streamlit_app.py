from collections import namedtuple
import re
import requests
import time
import math
import pandas as pd
import json
import streamlit as st
from PIL import Image


image = Image.open("Emicool_Logo.80kb_high_res-removebg-preview.png")
st.image(image)
"""
# Welcome to EmiGPT!

This tool is for Emicool employees only.





"""

def clean_text(text):
    new = str(text)
    new = new.replace("[{'generated_text':", "")
    new = new.replace("[{", "")
    new = new.replace("}]", "")
    new = new.replace("'", "")
    return new
# Hagging face API
API_URL = "https://api-inference.huggingface.co/models/grammarly/coedit-large"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	

txt = st.text_area('Enter your text here', '')
st.button("Improve writing", type="primary")

if txt:
    with st.spinner('Wait for it...'):
        output = query({"inputs": "Fix spelling, grammar and write this more professionally:" + txt, "options": {"wait_for_model":True}})
        cln_txt = clean_text(output)
        out_txt = st.text_area("", cln_txt)