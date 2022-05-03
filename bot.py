import pandas as pd
import numpy as np
import time
import streamlit as st

# Import and organize excel sheets into dataframes

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     df2 = pd.read_csv(uploaded_file)
     st.write("filename:", uploaded_file.name)
     st.write(df2)
