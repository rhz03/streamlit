# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import plotly.express as px


st.title('Data visualization and Interactive')


df=pd.read_csv("Student mental health.csv")
df=pd.DataFrame(df)
st.header('Mental health visualizations')

fig=px.bar(df, x="Panic _attack",
             color='gender', barmode='group',
             height=400,title="Number of panic attacks of males and females")
st.plotly_chart(fig)
fig = px.histogram(df, x="course",color='gender',histfunc="count",text_auto=True,title='Number of Course of each gender')
st.plotly_chart(fig)

df_male = df[df["gender"]=="Male"]
df_female = df[df["gender"]=="Female"]
df_age_male = df_male.groupby(["Age"], as_index = False)["Timestamp"].count()
df_age_female = df_female.groupby(["Age"], as_index = False)["Timestamp"].count()
fig = px.pie(df_age_male , values='Age', names='Age', title='Age Distribution for Males')
st.plotly_chart(fig)
fig = px.pie(df_age_female , values='Age', names='Age', title='Age Distribution for Females')
st.plotly_chart(fig)
health=pd.read_csv("healthy_lifestyle_city_2021 copy.csv")
st.header('Health lifestyle of cities(2021) visualizations')
fig=px.scatter(health,x="City",y="Sunshine hours(City)",title="Sunshine hours of Cities",color="City",hover_name="City")
st.plotly_chart(fig)
fig=px.box(health,y="Cost of a bottle of water(City)",title="Cost of a bottle of water Cities")
st.plotly_chart(fig)

option = st.radio(
    'Have you ever had a Panik attack?',
    ('yes','no'))
if option=="yes":
    Panik_attack=df[df["Panic _attack"]=="Panik_attack"]
    st.header('Find below a bar graph on number of females and males who had panik attack as a student')
    fig=px.bar(df, x="Panic _attack",
                 color='gender', barmode='group',
                 height=400,title="Number of panic attacks of males and females")
    
    st.plotly_chart(fig)
 
st.write('You selected:', option)
choice = st.selectbox(
    'Select the gender',
    ('Female', 'Male'))
if choice == 'Female':
  df_female = df[df["gender"]=="Female"]
  df_female_course = df_female.groupby(["course"], as_index = False)["Timestamp"].count()
  fig = px.bar(df_female_course, x = ['course'], title = 'Count of major for females')
  st.plotly_chart(fig)
else:
  df_male = df[df["gender"]=="Male"]
  df_male_course = df_male.groupby(["course"], as_index = False)["Timestamp"].count()
  fig = px.bar(df_male_course, x = ['course'], title = 'Count of major for males')
  st.plotly_chart(fig)
  
cost=st.slider("How much is the cost of bottle of water you buy?",0.00,3.00)    
if cost>=0.15 and cost<=2.11:
    fig=px.box(health,y="Cost of a bottle of water(City)",title="Cost of a bottle of water Cities")
    st.plotly_chart(fig)
    st.write("cost of bottle of water you buy is: €",cost)
