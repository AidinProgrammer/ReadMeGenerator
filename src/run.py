import streamlit as st
from pathlib import Path

def generate_profile(theme, **kwargs):
    with open(f"src/themes/{theme}/profile.txt") as f:
        profile = f.read()

    for item, value in kwargs.items():
        if not value:
            profile = profile.replace(f"{{ {item} }}", '')
            continue
        item_path = Path(f"src/themes/{theme}/{item}.txt")
        if not item_path.exists():
            continue
        with open(item_path) as f:
            profile_item = f.read().strip()
        profile_item = profile_item.replace("{ value }", value)
        profile = profile.replace(f"{{ {item} }}", profile_item)

    return profile

st.title(':adult: ReadMe Profile Creator')

kwargs= {}
# Getting the personal information
st.header('Personal Info')
with st.expander('Personal Info'):
    col1, col2 = st.columns(2)
    kwargs['name'] = col1.text_input('Name')
    kwargs['email'] = col2.text_input('Email')
    kwargs['phone'] = col1.text_input('Phone')
    kwargs['homepage'] = col2.text_input('Homepage address')
    kwargs['location'] = st.text_input('Location')

# Getting the social media
st.header('Social Media')
with st.expander('Social Media'):
    st.markdown('Please only write your username!')
    col1, col2 = st.columns(2)
    kwargs['github'] = col1.text_input('GitHub')
    kwargs['linkedin'] = col2.text_input('Linkedin')
    kwargs['twitter'] = col1.text_input('Twitter')
    kwargs['facebook'] = col2.text_input('Facebook')
    kwargs['youtube'] = col1.text_input('YouTube')
    kwargs['instagram'] = col2.text_input('Instagram')

# Getting the theme
st.header('Theme')
themes = list(Path('src/themes/').iterdir())
themes = [theme.name for theme in themes]
theme = st.selectbox('Select your theme', themes)
st.markdown(F'Your selected theme: **{theme}**')

# Generating ReadMe
st.header('Generate ReadMe')
profile = generate_profile(theme, **kwargs)
st.code(profile)