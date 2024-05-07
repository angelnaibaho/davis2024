import streamlit as st
import pandas as pd
 
st.write("""# Book Scrape""")
 
df = pd.read_csv("BookScrape.csv")
st.bar_chart(df)