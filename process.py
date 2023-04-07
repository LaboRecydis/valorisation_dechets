import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
#import matplotlib
#import matplotlib.pyplot as plt
#matplotlib.use('Agg')
import json
#import plotly.express as px
import altair as alt





if __name__=="__main__":
    st.set_page_config(
        page_title="Streamlit basics app",
        layout="centered"
    )

    st.title("Process de valorisation des emballages vides souillés")

    st.write("Auteur : Jenna TADJER  - Responsable Commerciale BTP ")
  
   
   
    # Display the LOGO
    img1 = Image.open("IMG_PAPREC.jpg")
    img2 = Image.open("IMG_RECYDIS.jfif") 
    
    st.sidebar.image(img1, width=250)
    st.sidebar.image(img2, width=250)


    st.write("Il existe plusieurs traitements des déchets:")
    st.write("         - le recyclage")
    st.write("         - le recyclage")
    st.write("         - La régénération")
    st.write("         - Le réemploi")
    st.write("         - La valorisation énergétique")
             
    


  
    


