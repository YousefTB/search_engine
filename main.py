import streamlit as st
from Search_Engine import SearchEngine

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.freepik.com/free-photo/ai-technology-microchip-background-digital-transformation-concept_53876-124669.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

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
        for i in range(len(result)):
            with st.expander(f"See Result {i + 2}"):
                st.write(result[i])