import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
# import altair as alt

#nav sidebar
with st.sidebar:
    selected = option_menu("Angel Dashboard", ['Rectangle Calculator', 'Box Office Scrap', 'Book Scrap'], 
        icons=['calculator', 'film', 'book'], menu_icon="house", default_index=0)
    
# Rect Calc
if (selected == 'Rectangle Calculator'): 
    st.title("Hitung Luas Persegi Panjang")

    panjang = st.number_input ("Masukkan Nilai Panjang", 0)
    lebar = st.number_input ("Masukkan Nilai Lebar", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = panjang * lebar
        st.write("Luas Persegi Panjang adalah = ",luas )
        st.success(f"Luas Persegi Panjang adalah = {luas}")

# MovieScrap
if (selected == 'Box Office Scrap'):
    st.write("""# Box Office Scrap""")
    
    # read dataframe dari file CSV
    df = pd.read_csv("BoxOfficeMojoScrap.csv")
    
    # Pilih kolom judul dan pendapatan
    df_selected = df[['Nama Distributor', 'Total Pendapatan']]
    
    # Atur kolom judul sebagai index (opsional)
    df_selected.set_index('Total Pendapatan', inplace=True)
    
    # Tampilkan grafik batang
    st.bar_chart(df_selected)

# Bookscrape

if selected == 'Book Scrap':
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








# if (selected == 'Book Scrap'):
 
#     st.write("""# Book Scrape""")

#     # read dataframe dari file CSV
#     df = pd.read_csv("BookScrape.csv")
    
#     # Pilih kolom judul dan pendapatan
#     df_selected = df[['TITLE', 'PRICE']]
    
#     # Atur kolom judul sebagai index (opsional)
#     df_selected.set_index('PRICE', inplace=True)
    
#     # Tampilkan grafik batang
#     st.bar_chart(df_selected)




# if (selected == 'Box Office Scrap'):
#     st.write("""# Box Office Scrap""")
    
#     # read dataframe dari file CSV
#     df = pd.read_csv("BoxOfficeMojoScrap.csv")
    
#     # Groupby nama distributor dan jumlahkan total pendapatannya
#     df_grouped = df.groupby('Nama Distributor')['Total Pendapatan'].sum().reset_index()
    
#     # Tampilkan grafik batang interaktif menggunakan Altair
#     chart = alt.Chart(df_grouped).mark_bar().encode(
#         x='Total Pendapatan',
#         y='Nama Distributor',
#         tooltip=['Nama Distributor', 'Total Pendapatan']
#     ).properties(
#         width=alt.Step(80)
#     ).interactive()
    
#     st.altair_chart(chart, use_container_width=True)




# SHOW ALL #
# if (selected == 'Box Office Scrap') :
#     st.write("""# Box Office Scrap""")
    
#     df = pd.read_csv("BoxOfficeMojoScrap.csv")
#     st.bar_chart(df)