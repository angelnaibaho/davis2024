import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)



# Initialize connection.
# conn = st.connection('mysql', type='sql', username=st.secrets["DB_USER"], password=st.secrets["DB_PASS"], host=st.secrets["HOST"], database=st.secrets["DB"])
# conn = st.connection(**st.secrets.db_credentials)
conn = st.connection("mydb", type="sql", autocommit=True)

# Perform query.
df = conn.query('SELECT EnglishPromotionName, StartDate, EndDate, MaxQty from dimpromotion limit 10;', ttl=600)

st.table(df)
# Print results.
# for row in df.itertuples():
#     st.write(f"{row.EnglishPromotionName} , {row.MaxQty} ")


# PLOT SCATTER
st.write("""# Data Visual""")
st.write("""Anna Vita Angelina Naibaho - 21082010135""")
# Load data
data = pd.read_csv("tips.csv")

# Create scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])

# Adding Title to the Plot
ax.set_title("Scatter Plot")

# Setting the X and Y labels
ax.set_xlabel('Day')
ax.set_ylabel('Tip')

# Add colorbar
plt.colorbar(scatter, ax=ax)

# Show plot
st.pyplot(fig)

# Nomor 2 
# Load data
data = pd.read_csv("tips.csv")

# Create bar chart
fig, ax = plt.subplots()
ax.bar(data['day'], data['total_bill'])

# Adding Title to the Plot
ax.set_title("Bar Chart")

# Setting the X and Y labels
ax.set_xlabel('day')
ax.set_ylabel('total_bill')

# Show plot
st.pyplot(fig)
