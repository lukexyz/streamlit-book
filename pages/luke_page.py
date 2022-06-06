import streamlit as st
import pandas as pd

# st.set_page_config(page_title="Luke's Page", page_icon="🌍")

st.title("Luke's Page")

df = pd.read_csv('tmp/users.csv')
st.dataframe(df)