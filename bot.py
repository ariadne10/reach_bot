import pandas as pd
import numpy as np
import time
import streamlit as st
$ pip install openpyxl

# Import and organize excel sheets into dataframes

st.title("REACH Reports")

df = pd.read_excel("sheets/SKU list 040522.xlsx")
st.table(df)
