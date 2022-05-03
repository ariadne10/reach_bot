import pandas as pd
import numpy as np
import time
import streamlit as st

# Import and organize excel sheets into dataframes

uploaded_file = st.file_uploader(“Choose a file”)
if uploaded_file is not None:
     df1=pd.read_csv(uploaded_file)
     df1=pd.read_excel(uploaded_file)
else:
     st.warning(“you need to upload a csv or excel file.”)
 
