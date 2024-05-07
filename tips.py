import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
