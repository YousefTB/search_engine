import streamlit as st
from Search_Engine import SearchEngine

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www6.0zz0.com/2024/05/10/23/578888797.jpg");
    }
   </style>
    """,
    unsafe_allow_html=True
)

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