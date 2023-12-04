import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
# from streamlit_option_menu import option_menu
import subprocess
import os

# from util import classify, set_background

def main():
    st.set_page_config(
    page_title="Diagnosis at Home",
    page_icon="👨‍⚕️",
)

st.write("# Welcome to Diagnostics Report Analysis! 👋")
# set_background("bgs/doc1.png")

# sidebar for navigation, idk how to connect side bar to the pages
#with st.sidebar:

    #selected = option_menu('Diseases Prediction System',

                          #['COVID19 Prediction',
                           #'Brain Tumor Prediction'],
                          #icons=['mask','heart'],
                          #menu_icon="cast",
                          #default_index=0,
                          #orientation="horizontal")
st.markdown(
    """
    Diagnostics Report Analysis is a free app that we created in the hope of
    making the diagnostic process more readily available and to help our customers
    in analysing their diagnosis reports from their smart phones.

    **👈 Select a diagnostic method from the sidebar** and get an accurate prediction for COVID19 Chest X-Ray.
    ### What's our goal 🎯?
    - Avail the ability to detect COVID19 Chest X-Ray from your smart phones.
    - Reducing the Stress from over worked health professionals.
    - Providing a better understanding of the diagnosis.
    - Include more diagnostics reports analysis in future.
    - Prediction of Diseases based on your symptoms. (Just Like a Virtual Doctor)

    ### Sources:
    - Dataset for COVID19 [Covid19 detection using Tensorflow from Chest Xray](https://www.kaggle.com/code/ankan1998/covid19-detection-using-tensorflow-from-chest-xray/notebook)
    - Dataset for Brain tumor's [MRI](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)
"""
)

if st.button("Proceed"):
    subprocess.Popen(['streamlit', 'run', './pages/COVID19_Report.py'])
    os._exit(0)

# if __name__ == "__main__":
#     main()
