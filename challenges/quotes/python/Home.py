# coding: utf-8
"""hackatal2023 - UI.

An UI for the hackatal2023 POC build with https://docs.streamlit.io/
"""
import streamlit as st

st.set_page_config(
    page_title="HackaTAL 2023",
    layout="wide",
)

st.sidebar.success("Select a page to view.")

with st.container():
    st.title("HackaTAL 2023 - Détection de Citations.")
    st.header("Dashboard")
    st.markdown("""
    ![Bannière HackaTAL](https://raw.githubusercontent.com/HackaTAL/2023/gh-pages/HackaTAL_2023.png)
    """)
