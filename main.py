import streamlit as st
from Search_Engine import SearchEngine

if "my_engine" not in st.session_state:
    st.session_state['my_engine'] = SearchEngine()
    

text_input = st.text_input("Search bar", value=None, max_chars=256, key="text1", placeholder="بتدوّر على إيه ؟")
button1_clicked = st.button("Search", key='button1')
if button1_clicked:
    result = st.session_state['my_engine'].find(text_input, 2)
    for i in range(len(result)):
        with st.expander(f"See Result {i + 1}"):
            st.write(result[i])