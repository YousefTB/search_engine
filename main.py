import streamlit as st
from Search_Engine import SearchEngine

st.set_page_config(page_title="Dynamo SearchEngine", page_icon="photos/icon.png", menu_items={"About":"""Creator: Yousef Elbaroudy

Email: yousef.elbaroudy02@gmail.com"""})

c1, c2, c3 = st.columns([1,30,1])
with c2:
    st.title("Dynamo Search Engine")
    st.image('photos/bfcai.png', caption="Faculty of Computers and Artificial Intelligence")

if "my_engine" not in st.session_state:
    st.session_state['my_engine'] = SearchEngine()
    
tab1, tab2 = st.tabs(["Boolean Search", "FasterAI Search"])
with tab1:
    text_input = st.text_input("Search bar", value=None, max_chars=256, key="text1", placeholder="بتدوّر على إيه ؟")
    col1, col2, col3 = st.columns([5,2,5])
    with col2:
        button1_clicked = st.button("Search", key='button1')
        
    if button1_clicked and text_input != None:
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
        
    if button1_clicked and text_input != None:
        with st.spinner("Searching ..."):
            result = st.session_state['my_engine'].find(text_input, 2)
            
        with st.container(border=True):
            for i in range(len(result)):
                with st.expander(f"See Result {i + 1}"):
                    st.write(result[i])
                    
                    
with st.container(border=True):
    cc1, cc2, cc3 = st.columns([1,10,1])
    with cc2:
        st.header("Created by:")
        st.markdown('''
        :red[Yousef Elbaroudy]

        Email: yousef.elbaroudy02@gmail.com
        
        Github Profile: https://github.com/YousefTB''')