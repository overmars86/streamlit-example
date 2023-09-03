from collections import namedtuple
import re
import requests
import time
import math
import pandas as pd
import json
import streamlit as st

"""
# Welcome to EmiGPT!

This tool is for Emicool employees only.





"""

def clean_text(text):
    new = text.replace("[{'generated_text':", "")
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
        output = query({"inputs": "Write this more formally:" + txt, "options": {"wait_for_model":True}})
        nor_str = json.dumps(output)
        new = nor_str.replace("[{'generated_text':", "")
        new = new.replace("[{", "")
        new = new.replace("}]", "")
        new = new.replace("'", "")
        out_txt = st.text_area("", new)