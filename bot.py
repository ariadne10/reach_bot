import pandas as pd
import numpy as np
import time
import streamlit as st
import pip
import matplotlib.pyplot as plt

pip.main(["install", "openpyxl"])

# Import and organize excel sheets into dataframes

st.title("REACH Reports")

st.sidebar.subheader("Visualization Settings")

# Setup File Upload
df1 = st.sidebar.file_uploader(label="Upload EU Sales",
                                         type=['csv', 'xlsx'])

if df1 is not None:
  print(df1)
  print('hello')
  try:
    df1 = pd.read_csv(df1)
  except Exception as e:
    print(e)
    df1 = pd.read_excel(df1)
try:
  pass
except Exception as e:
  print(e)
  st.write("Please upload your files")
            
    
    
    
df2 = st.sidebar.file_uploader(label="Upload SKU List",
                                         type=['csv', 'xlsx'])

if df2 is not None:
  print(df2)
  print('hello')
  try:
    df2 = pd.read_csv(df2)
  except Exception as e:
    print(e)
    df2 = pd.read_excel(df2)
try:
  df2 = df2[["Material Number", "FY22 Forecast"]]
except Exception as e:
  print(e)
  st.write("Please upload your files")
    
   
  

df3 = st.sidebar.file_uploader(label="Upload REACH",
                                         type=['csv', 'XLSX'])


if df3 is not None:
  print(df3)
  print('hello')
  try:
    df3 = pd.read_csv(df3)
  except Exception as e:
    print(e)
    df3 = pd.read_excel(df3, sheet_name = 'Master')
try:
  df3 = pd.read_excel(df3, sheet_name = 'Master')
  df3 = df3.dropna()
  df3 = df3[["Material", "Component", "Quantity"]].sort_values(by='Component').reset_index()
  df3 = df3.drop(df3.columns[0], inplace=True, axis=1)
except Exception as e: 
  print(e)
                                         


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

############################################## FY22 FORECAST ####################################################

# Merge df2 & df3 values based on identical Materials

df3 = df3.merge(df2, left_on='Material', right_on='Material Number', how='inner')


# Show columns needed

df3 = df3[["Material", "Component", "Quantity", "FY22 Forecast"]].sort_values(by='Component').reset_index()

df3.drop(df3.columns[0], inplace=True, axis=1)

df3.columns = [c.replace(' ', '_') for c in df3.columns]


# (Forecast * Quantity) / 1000 = FY22 BOM

df3['REACH'] = (df3.Quantity * df3.FY22_Forecast)/1000


# Create dictionary with Components as Keys and FY22 BOM #'s as Values

df3 = df3.groupby('Component').REACH.apply(list).to_dict()


# Sum the BOM #'s in each component

final = dict(zip(df3.keys(), [[sum(item)] for item in df3.values()]))


# Turn dictionary into dataframe 

final = pd.DataFrame.from_dict(final, orient ='index').reset_index()


# Rename columns

final = final.rename(columns={"index": "Component", 0: "REACH FY22"})

# Sort values in descending order

final = final.sort_values(by="Component", ascending=True)
 

# Add date to file export

#timestr = time.strftime(" %m-%d-%Y")


# Combine FY21 Usage & REACH FY22

data = {'Component' : final1['Component'], 'FY21 Usage':final1['FY21 Usage'], 'REACH FY22':final['REACH FY22']}

df = pd.DataFrame(data)


# Show columns > 750 (& = and) (| = or)

df_mask = df[(df['FY21 Usage']>= 750) | (df['REACH FY22']>= 750)].reset_index()

df_mask.drop(df_mask.columns[0], inplace=True, axis=1)
             
df_mask

# Bar Chart
chart_data = pd.DataFrame(
     columns = list(df_mask['Component']),
     np.random.randn(50, 30))

st.bar_chart(chart_data)




