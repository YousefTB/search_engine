import streamlit
from Search_Engine import SearchEngine

text_input = st.text_input("Search bar", value=None, max_chars=256, key="text1", placeholder="بتدوّر على إيه ؟")