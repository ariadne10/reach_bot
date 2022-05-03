import pandas as pd
import numpy as np
import time
import streamlit as st
import pip
pip.main(["install", "openpyxl"])

# Import and organize excel sheets into dataframes

st.title("REACH Reports")


df1 = pd.read_excel("sheets/EU Sales FY21.xlsx")

df2 = pd.read_excel("sheets/SKU list 040522.xlsx")
df2 = df2[["Material Number", "FY22 Forecast"]]


df3 = pd.read_excel("sheets/REACH Report 040522.XLSX", sheet_name='Master')
df3.drop(df3.columns[0], inplace=True, axis=1)

############################################## FY21 USAGE ####################################################

# Merge df2 & df3 values based on identical Materials

df10 = df3.merge(df1, left_on='Material', right_on='Material', how='inner')


# Show columns needed

df10 = df10[["Material", "Component", "Quantity", "Tot. usage"]].sort_values(by='Component').reset_index()

df10.drop(df10.columns[0], inplace=True, axis=1)

df10.columns = [c.replace(' ', '_') for c in df10.columns]

df10.columns = [c.replace('.', '_') for c in df10.columns]

# (Forecast * Quantity) / 1000 = FY22 BOM

df10['REACH'] = (df10.Quantity * df10.Tot__usage)/1000


# Create dictionary with Components as Keys and FY22 BOM #'s as Values

df10 = df10.groupby('Component').REACH.apply(list).to_dict()


# Sum the BOM #'s in each component

final1 = dict(zip(df10.keys(), [[sum(item)] for item in df10.values()]))


# Turn dictionary into dataframe 

final1 = pd.DataFrame.from_dict(final1, orient ='index').reset_index()


# Rename columns

final1 = final1.rename(columns={"index": "Component", 0: "FY21 Usage"})

# Sort values in descending order

final1 = final1.sort_values(by="Component", ascending= True)


