import seaborn as sns
df = sns.load_dataset("penguins")
import streamlit as st

st.title("Penguins")
st.write(df)



# pip install seaborn
# py -m pip install seaborn