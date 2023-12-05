import streamlit as st
# from keras.models import load_model
from PIL import Image
import numpy as np
from util import *
# from util import predict
import requests

# COVID19 Prediction Page
set_background ("pages/covid.jpg")

# set title
st.markdown("<h1><span style='color: black;'>COVID19 CHEST X-RAY</span> <span style='color: black;'>ANALYSIS</span></h1>", unsafe_allow_html=True)

# set header
st.markdown("<h2 style='color: white;'>Please Upload or Scan An X-Ray Image.</h2>", unsafe_allow_html=True)

# upload file
uploaded_file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load model
# model = load_model('../model/3')

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("<h3 style='color: red;'>RESULT</h3>", unsafe_allow_html=True)

    # Prepare image for API
    # files = {"image": uploaded_file.getvalue()}
    image_byte = uploaded_file.read()
    # breakpoint()
    response = requests.post("https://diagnostic-mv6hb5oqca-ew.a.run.app/predict", files={'file': image_byte})

    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)

    if response.status_code == 200:
        result = response.json()
        # st.write(f"COVID Probability: {result['covid_probability']}")
        if result['Confidence']> 0.60:
            st.write("<h3 style='color: yellow;'>This Chest X-Ray Shows That The Patient is COVID Positive!</h3>", unsafe_allow_html=True)
        else:
             st.write(f"<h3 style='color: yellow;'>This Chest X-Ray Shows That The Patient is COVID Negative!</h3>", unsafe_allow_html=True)

    else:
        st.write("<h3 style='color: yellow;'>Error predicting. Please try again.</h3>", unsafe_allow_html=True)
        # st.write(result['Confidence'], unsafe_allow_html=True)

# load class names
# with open('../model/labels.txt', 'r') as f:
#     class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
#     f.close()

# def image
# if file is not None:
#     image = Image.open(file).convert('RGB')
#     st.image(image, use_column_width=True)

# if st.button("Submit"):
#     classify image
#     predict.Class, predict.Confidence = classify("Normal", "PNEUMONIA")

    # write classification
    # st.write("## {}".format('predict.Class'))
    # st.write("### score: {}%".format(float(('predict.Confidence') * 1000) / 10))
