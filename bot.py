import pandas as pd
import numpy as np
import time
import streamlit as st

# Import and organize excel sheets into dataframes

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     df2 = pd.read_csv(uploaded_file)
     st.write(df2)
