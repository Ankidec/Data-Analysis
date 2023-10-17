import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Smokers Dashboard")
st.markdown("The dashboard will help a researchers to get to know more about the given dataset and it's output")

st.sidebar.title("Select Vishul Charts")
st.sidebar.markdown("Select the Chats/Plots accordingly:")

#Reading the dataset 
data=pd.read_csv(r"C:\Users\PS3\Documents\Data Analysis\demo_data_set.csv")

chart_visual = st.sidebar.selectbox("Select the Charts/Plots",('Line Charts', 'Bar Charts','Buble Charts'))

#st.sidebar.checkbox("Show Analysis by Smoking Status ", True, Key=1)
selected_status=st.sidebar.selectbox("Select Smoking Status", options=['formly_smoked','Smokes','Never_Smoked','Unknown'])

fig = go.figure()
if chart_visual == 'Line Charts':
  if selected_status =='formerly_smoked':
     fig.add_trace(go.Scatter(x=data.Country, y=data.formerly_smoked, mode='lines',name='formerly_smoked'))

if selected_status =='Smoked':
     fig.add_trace(go.Scatter(x=data.Country, y=data.Smoked, mode='lines',name='Smoked'))
 
if selected_status =='Nover_smoked':
     fig.add_trace(go.Scatter(x=data.Country, y=data.Nover_smoked, mode='lines',name='Nover_smoked'))

if selected_status =='Unknown':
     fig.add_trace(go.Scatter(x=data.Country, y=data.Unknown_smoked, mode='lines',name='Unknown_smoked'))

elif chart_visual =='Bar chart':
  if selected_status == 'formerly_smoked':
      fig.add_trace(go.Scatter(x=data.country,y=data.formerly_smoked, name='formerly_smoked'))

if selected_status == 'Smoked':
      fig.add_trace(go.Scatter(x=data.country,y=data.Smoked, name='Smoked'))

if selected_status == 'Never_smoked':
      fig.add_trace(go.Scatter(x=data.country,y=data.Never_smoked, name='Never_smoked'))

if selected_status == 'Unknown_smoked':
      fig.add_trace(go.Scatter(x=data.country,y=data.Unknown_smoked, name='Unknown_smoked'))

elif chart_visual =='Bubble_chart':
   if selected_status == 'formerly_smoked':
      fig.add_trace(go.Scatter(x=data.country,y=data.formerly_smoked, name='formerly_smoked'))

if selected_status == 'Smoked':
      fig.add_trace(go.Scatter(x=data.country,y=data.Smoked, name='Smoked'))

if selected_status == 'Never_smoked':
      fig.add_trace(go.Scatter(x=data.country,y=data.Never_smoked, name='Never_smoked'))

if selected_status == 'Unknown_smoked':
      fig.add_trace(go.Scatter(x=data.country,y=data.Unknown_smoked, name='Unknown_smoked'))

st.plotly_chart(fig, use_container_width=True)



