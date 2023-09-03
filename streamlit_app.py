from collections import namedtuple
import altair as alt
import time
import math
import pandas as pd
import streamlit as st

"""
# Welcome to EmiGPT!

This tool is for Emicool employees only.





"""

txt = st.text_area('Enter your text here', '')
st.button("Improve writing", type="primary")
with st.spinner('Wait for it...'):
    time.sleep(5)