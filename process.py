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
    img3= Image.open("echantillon.jpg")
    img4= Image.open("procedure.jpg")
    img5= Image.open("réactifs.jpg")
    img6= Image.open("resultat.jpg")
    st.sidebar.image(img1, width=250)
    st.sidebar.image(img2, width=250)


    st.write("CONCLUSION: aucune coloration observée, pas de présence de cyanures")
    


  
    


