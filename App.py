import streamlit as st
st.set_page_config(
        page_title="Neural Sims - Krish Suraparaju", 
        page_icon=":brain:"
    )

# Custom imports 
from Multipage import MultiPage
from pages import Oscillating_Network_ST_page, Simple_Learning_Network_ST_Page, Home_Page

# Create an instance of the app 
app = MultiPage()
 

# Title of the main page

# Add all your applications (pages) here
app.add_page("Home Page", Home_Page.app)
app.add_page("Oscillating Circuit (Small Population)", Oscillating_Network_ST_page.app)
app.add_page("Simple Learning Circuit (Large Populatio)",Simple_Learning_Network_ST_Page.app)

# The main app
app.run()