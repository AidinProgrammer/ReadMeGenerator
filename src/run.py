import streamlit as st

st.title(':adult: ReadMe Profile Creator')

# Getting the personal information
st.header('Personal Info')
with st.expander('Personal Info'):
    col1, col2 = st.columns(2)
    name = col1.text_input('Name')
    email = col2.text_input('Email')
    phone = col1.text_input('Phone')
    homepage = col2.text_input('Homepage address')
    location = st.text_input('Location')

# Getting the social media
st.header('Social Media')
with st.expander('Social Media'):
    st.markdown('Please only write your username!')
    col1, col2 = st.columns(2)
    github = col1.text_input('GitHub')
    linkedin = col2.text_input('Linkedin')
    twitter = col1.text_input('Twitter')
    facebook = col2.text_input('Facebook')
    youtube = col1.text_input('YouTube')
    instagram = col2.text_input('Instagram')