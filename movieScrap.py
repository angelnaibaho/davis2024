import streamlit as st
import pandas as pd
 
st.write("""# Book Scrap""")
    
# read dataframe dari file CSV
df = pd.read_csv("BookScrape.csv")

# Pilih kolom judul dan harga
df_selected = df[['TITLE', 'PRICE']]

# Buat scatter plot dengan Plotly Express
fig = px.scatter(df_selected, x='PRICE', y='TITLE')

# Konfigurasi tampilan scatter plot
fig.update_traces(marker=dict(size=5, color='skyblue', opacity=1), selector=dict(mode='markers'))

# Menampilkan scatter plot
st.plotly_chart(fig)
