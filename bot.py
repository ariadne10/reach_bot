import pandas as pd
import numpy as np
import time
import streamlit as st
import pip
pip.main(["install", "openpyxl"])

# Import and organize excel sheets into dataframes

st.title("REACH Reports")

df1 = pd.read_excel("sheets/EU Sales FY21.xlsx")
st.table(df1)

df2 = pd.read_excel("sheets/SKU list 040522.xlsx")
st.table(df2)

df3 = pd.read_excel("sheets/REACH Report 04-05-22.xlsx")
st.table(df3)
