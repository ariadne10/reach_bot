import pandas as pd
import numpy as np
import time
import streamlit as st
import pip
pip.main(["install", "openpyxl"])

# Import and organize excel sheets into dataframes

st.title("REACH Reports")



df3 = pd.read_excel("sheets/REACH Report 040522.XLSX")
st.table(df3)
