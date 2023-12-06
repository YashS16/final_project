import streamlit as st
# from keras.models import load_model
# from PIL import Image
# import numpy as np
from streamlit import option_menu
from util import set_background, on_change
# from streamlit_modal import Modal
# from streamlit_extras.switch_page_button import switch_page
import subprocess
import os
# from google.oauth2 import id_token
# from google.auth.transport import requests
# from brain import MRI


#Menu
selected = option_menu(None, ["Home", "About Us", "Covid", "Brain"],
                    icons=['house', "people", 'lungs', "f5dc"],
                    on_change=on_change, key='menu_4', orientation="horizontal")

if selected =="Home":
    #st.rerun() or st.experimental_rerun()
    print('Yes')
#if selected == "About us":
    #subprocess.Popen(["streamlit", "run", ".py"])
    #os._exit(0)
if selected == "Covid":
    subprocess.Popen(["streamlit", "run", "pages/COVID19_Report.py"])
    os._exit(0)
if selected == "Brain":
    subprocess.Popen(["streamlit", "run", "BRAIN_MRI.py"])
    os._exit(0)


def Home():
    st.set_page_config(
        page_image(os.path.join(os.path.dirname(__file__),"..", "pages", "SmartDiag Tech.png")),
        page_title="SmartDiag Tech",
        page_icon="👨‍⚕️"
        )

st.write("# Welcome to SmartDiag Tech 👋")

def set_background():
    set_background(os.path.join(os.path.dirname(__file__),"..", "pages", "home_page.png"))


st.markdown(
    """
    Diagnostics Report Analysis is a free app that we created in the hope of
    making the diagnostic process more readily available and to help our customers
    in analysing their diagnosis reports from their smart phones.
    """
)


# if __name__ == '__main__':
#     main()
