import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
import requests
from util import set_background
from streamlit_option_menu import option_menu
import subprocess
from util import set_background, on_change
import os

#Menu
selected = option_menu(None, ["Home", "About Us", "Covid", "Brain"],
                    icons=['house', "people", 'lungs', "f5dc"],
                    on_change=on_change, key='menu_4', orientation="horizontal")

if selected =="Home":
    #st.rerun() or st.experimental_rerun()
    print('Yes')
if selected == "Covid":
    subprocess.Popen(["streamlit", "run", "pages/COVID19_Report.py"])
    os._exit(0)
if selected == "Brain":
    subprocess.Popen(["streamlit", "run", "pages/BRAIN_MRI.py"])
    os._exit(0)
#if selected == "About us":
    #subprocess.Popen(["streamlit", "run", ".py"])
    #os._exit(0)

# COVID19 Prediction Page
set_background(os.path.join(os.path.dirname(__file__),"..", "pages", "mri_scan.png"))

# set title
st.markdown("<h1><span style='color: black;'>Brain tumor</span> <span style='color: black;'>Detection</span></h1>", unsafe_allow_html=True)

# set header
st.markdown("<h2 style='color: white;' >Please upload or drop a brain's MRI image.</h2>", unsafe_allow_html=True)

# upload file
uploaded_file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("<h3 style='color: red;'>RESULT</h3>", unsafe_allow_html=True)

    # Prepare image for API
    image_byte = uploaded_file.read()

    response = requests.post("https://diagnosticreportprediction-mv6hb5oqca-ew.a.run.app/predict", files={'file': image_byte})

    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)

    if response.status_code == 200:
        result = response.json()
        if result['Class'] ==  "meningioma_tumor":
            st.write("<h3 style='color: yellow;'>This Brain MRI Shows Meningioma Tumor!</h3>", unsafe_allow_html=True)
        elif result['Class'] == "glioma_tumor":
            st.write(f"<h3 style='color: yellow;'>This Brain MRI Shows Glioma Tumor!</h3>", unsafe_allow_html=True)
        elif result['Class'] == "no_tumor":
            st.write(f"<h3 style='color: yellow;'>This Brain MRI Shows No Tumor!</h3>", unsafe_allow_html=True)
        elif result['Class'] == "pituitary_tumor":
            st.write(f"<h3 style='color: yellow;'>This Brain MRI Shows Pituitary Tumor!</h3>", unsafe_allow_html=True)

    else:
        st.write("<h3 style='color: yellow;'>Error predicting. Please try again.</h3>", unsafe_allow_html=True)
