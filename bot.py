import pandas as pd
import numpy as np
import time
import streamlit as st
import pip
pip.main(["install", "openpyxl"])

# Import and organize excel sheets into dataframes

st.title("REACH Reports")

df2 = pd.read_excel("sheets/SKU list 040522.xlsx")
st.table(df2)
