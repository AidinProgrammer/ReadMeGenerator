import streamlit as st

# Getting the personal information
st.title('Personal Info Creator')
with st.expander('Personal Info'):
    col1, col2 = st.columns(2)
    name = col1.text_input('Name')
    email = col2.text_input('Email')
    phone = col1.text_input('Phone')
    homepage = col2.text_input('Homepage address')
    location = st.text_input('Location')