from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import base64
import streamlit as st
import os

def set_background(image_file):
    """
    This function sets the background of a Streamlit app to an image specified by the given image file.
    Parameters:
        image_file (str): The path to the image file to be used as the background.
    Returns:
        None
    """
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
            background-attachment: scroll;
            opacity: 0.8
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

app = FastAPI()

endpoint = "https://diagnostic-mv6hb5oqca-ew.a.run.app/"
# MODEL = tf.keras.models.load_model('/Users/yashshrivastava/code/YashS16/final_project/app/model/model.h5')
# MODEL = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__),"..", "model", "3"))
CLASS_NAMES = ['NORMAL', 'PNEUMONIA']

@app.get('/')
def ping():
    # load a machine learning model
    # model.predict
    return {"ok": True}
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)).resize((244, 244)))
    return image
@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
    ):
    # breakpoint()
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    my_img = np.stack((img_batch,) * 3, axis=-1)
    prediction = MODEL.predict(my_img)
    prediction_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    return {
         'Class': prediction_class,
         'Confidence': float(confidence)
     }

# # Horizontal menu
# def on_change(key):
#     selection = st.session_state[key]
