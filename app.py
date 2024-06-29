import streamlit as st
from st_pages import Page, show_pages


st.set_page_config(
    layout="centered", page_title="SES", page_icon="static/doco_logo.jpg"
)

show_pages(
    [
        Page("views/home.py", "🏠 Home"), 
        Page("views/main.py", "🔬 Main Page"), 
        Page("views/about.py", "🔎 Explorers Story"), 
        Page("views/contact.py", "📨 Contact Us")
    ]
)
