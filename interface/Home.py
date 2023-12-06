import streamlit as st
from streamlit_option_menu import option_menu
# from keras.models import load_model
# from PIL import Image
# import numpy as np
from util import *
# from streamlit_modal import Modal
# from streamlit_extras.switch_page_button import switch_page
import subprocess
import os
# from google.oauth2 import id_token
# from google.auth.transport import requests
# from brain import MRI

st.write("# Welcome to SmartDiag Tech 👋")

# set_background(os.path.join(os.path.dirname(__file__),"..", "pages", "home_page.png"))


st.markdown(
    """
    Diagnostics Report Analysis is a free app that we created in the hope of
    making the diagnostic process more readily available and to help our customers
    in analysing their diagnosis reports from their smart phones.
    """
)


# if __name__ == '__main__':
#     main()
