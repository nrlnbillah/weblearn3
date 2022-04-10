import streamlit as st
import numpy as np
import pandas as pd
import plotly_express as px

### Import data frame
data_raw = pd.read_csv("ramen-ratings.csv")

ramen_data_raw = pd.read_csv("ramen-ratings.csv")
ramen_data_raw.drop(['Review', 'Variety','Top Ten'], axis = 1, inplace = True)
newcol = ['Brand', 'Style', 'Country', 'Stars']

df = ramen_data_raw.rename(columns = dict(zip(ramen_data_raw.columns, newcol)))
df['Stars'] = df['Stars'].replace('[%,]', '', regex=True).astype(float)
pd.options.display.float_format = "{:,.2f}".format
df['Style'] = df['Style'].apply(lambda x: str(x))


### --- 'Home' page

col1, col2 = st.columns([2, 1])

with col1:
  st.write("""
  # Ramen Ratings
  
  #### This web app analyses **Ramen Ratings** dataset!
  
  Disclaimer:  
  This is a web app using python libraries for learning purpose only.
  """)

with col2:
  st.write("")
  st.write("")
  st.write("")

st.write("")
st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html).')

show = st.checkbox('I agree the terms and conditions.')
st.write("")
st.write("")

if show:


### --- Sidebar layout

    st.sidebar.write(
       """Credits to:  
        - Ts. Dr. Yong Poh Yu  
        - Dr. Tan Yan Bin"""
    )
    
    st.sidebar.write('')
    

    ### --- Sidebar selectbox
    option = st.sidebar.selectbox(
        'Select your page',
        ['Dataset', 'Scatterplot', 'Histogram'])
    

    #### --- Option 'Dataset'
    if option=='Dataset':
      st.subheader('Dataset')
      st.write(
          """Source:  
        Kaggle ([Ramen Ratings](https://www.kaggle.com/datasets/residentmario/ramen-ratings))"""
        )
      st.write('')
      show2 = st.checkbox('Display raw data.')
      if show2:
        st.write(data_raw)
        st.write("")      
      st.write(df)
      st.write('')
      st.write(df.describe())

    #### --- Option 'Scatterplot'  
    if option=='Scatterplot':
      x_axis = st.sidebar.selectbox(
          'x-axis',options = list(df.columns))
      y_axis = st.sidebar.selectbox(
          'y-axis', options = list(df.columns))
      scatterplot = px.scatter(data_frame = df, x = x_axis, y = y_axis)
      st.plotly_chart(scatterplot)

    #### --- Option 'Histogram'    
    if option=='Histogram':
      x_axis = st.sidebar.selectbox(
          'x-axis', options = list(df.columns))
      y_axis = st.sidebar.selectbox(
          'y-axis', options = list(df.columns))
      histo = px.histogram(data_frame = df, x = x_axis, y = y_axis)
      st.plotly_chart(histo)
