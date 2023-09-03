from collections import namedtuple
import altair as alt
import re
import requests
import time
import math
import pandas as pd
import streamlit as st

"""
# Welcome to EmiGPT!

This tool is for Emicool employees only.





"""

def clean_text(text):
    new = text.replace('generated_text:',"")
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
        output = query({f"inputs": "Write this more formally:f{txt}", "options": {"wait_for_model":True}})
        # cln_txt = clean_text(output)
        out_txt = st.text_area("", output)