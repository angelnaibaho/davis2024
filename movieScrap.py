import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("BoxOfficeMojoScrap.csv")
st.bar_chart(df)