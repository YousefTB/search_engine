import streamlit as st
from Search_Engine import SearchEngine

c1, c2, c3 = st.columns([5,2,5])
with c2:
    st.image('photo/bfcai.png', caption="Faculty of Computer and Artificial Intelligence")

if "my_engine" not in st.session_state:
    st.session_state['my_engine'] = SearchEngine()
    
tab1, tab2 = st.tabs(["Boolean Search", "FasterAI Search"])
with tab1:
    text_input = st.text_input("Search bar", value=None, max_chars=256, key="text1", placeholder="بتدوّر على إيه ؟")
    col1, col2, col3 = st.columns([5,2,5])
    with col2:
        button1_clicked = st.button("Search", key='button1')
        
    if button1_clicked:
        with st.spinner("Searching ..."):
            result = st.session_state['my_engine'].find(text_input, 1)
            
        with st.container(border=True):
            for i in range(len(result)):
                with st.expander(f"See Result {i + 1}"):
                    st.write(result[i])
                
with tab2:
    text_input = st.text_input("Search bar", value=None, max_chars=256, key="text2", placeholder="بتدوّر على إيه ؟")
    col1, col2, col3 = st.columns([5,2,5])
    with col2:
        button1_clicked = st.button("Search", key='button2')
        
    if button1_clicked:
        with st.spinner("Searching ..."):
            result = st.session_state['my_engine'].find(text_input, 2)
            
        with st.container(border=True):
            for i in range(len(result)):
                with st.expander(f"See Result {i + 1}"):
                    st.write(result[i])