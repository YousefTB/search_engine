import streamlit as st
from Search_Engine import SearchEngine

page_bg_img = '''
<style>
body {
background-image: url("https://drive.google.com/file/d/14XDz57WVyJEkoD7nCvE6zVCxUVLxLBnJ/view?usp=drive_link");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

if "my_engine" not in st.session_state:
    st.session_state['my_engine'] = SearchEngine()
    

text_input = st.text_input("Search bar", value=None, max_chars=256, key="text1", placeholder="بتدوّر على إيه ؟")
button1_clicked = st.button("Search", key='button1')
if button1_clicked:
    with st.spinner("Searching ..."):
        result = st.session_state['my_engine'].find(text_input, 2)
    for i in range(len(result)):
        with st.expander(f"See Result {i + 1}"):
            st.write(result[i])