import streamlit as st
st.set_page_config(
        page_title="Neural Sims - Krish Suraparaju", 
        page_icon=":brain:"
    )

# Custom imports 
from Multipage import MultiPage
from pages import Home_Page, Oscillating_Network_ST_page, Diverging_Circuit_page, Simple_Learning_Network_ST_Page, Reverbating_Circuit_Page

# Create an instance of the app 
app = MultiPage()
 

# Title of the main page

# Add all your applications (pages) here
app.add_page("Home Page", Home_Page.app)
app.add_page("Diverging/Converging Circuits", Diverging_Circuit_page.app)
app.add_page("Reverberating Circuit", Reverbating_Circuit_Page.app)
app.add_page("Oscillating Circuit (Small Population)", Oscillating_Network_ST_page.app)
app.add_page("Simple Learning Circuit (Large Populatio)",Simple_Learning_Network_ST_Page.app)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# The main app
app.run()