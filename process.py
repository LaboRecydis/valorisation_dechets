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
    img3 = Image.open("process_val.jpg")
    
    st.sidebar.image(img1, width=250)
    st.sidebar.image(img2, width=250)


    st.write("Il existe plusieurs traitements des déchets:")
   
    st.write("         - le recyclage")
    st.write("         - La régénération")
    st.write("         - Le réemploi")
    st.write("         - La valorisation énergétique")
    
    st.write(" Pour les emballages vides souillés, il s'agit d'une valorisation énergétique")
    st.write("Lorsqu’un déchet ne peut plus être exploité pour sa matière et qu’il n’est pas recyclable, la solution est la valorisation énergétique. Le déchet est transformé en énergie comme la chaleur, l’électricité ou le carburant. Cette solution se substitue aux énergies fossiles")

    st.write("La valorisation dans son ensemble, dont le but est que des déchets soient utilisés en substitution à d’autres matières ou produits, est aussi un type de traitement des déchets. Cependant, le traitement des déchets n’est pas le même suivant leur nature.")
             
    st.image(img3, width=900)


  
    


