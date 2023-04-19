import streamlit as st
from sklearn.datasets import load_iris

data = load_iris()
st.write(data)