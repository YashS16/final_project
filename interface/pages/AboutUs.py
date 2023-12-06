import streamlit as st
from util import set_background, on_change
import subprocess
import os
from streamlit_option_menu import option_menu


# #Menu
# selected = option_menu(None, ["Home", "Covid", "Brain", "About us" ],
#                     icons=['house', 'lungs', "f5dc", "people"],
#                     on_change=on_change, key='menu_4', orientation="horizontal")

# if selected =="Home":
#     #st.rerun() or st.experimental_rerun()
#     print('Yes')
# if selected == "Covid":
#     subprocess.Popen(["streamlit", "run", "covid.py"])
#     os._exit(0)
# if selected == "Brain":
#     MRI()
# if selected == "About us":
#     subprocess.Popen(["streamlit", "run", "aboutus.py"])
#     os._exit(0)

def about():
    st.write("# More about SmartDiag Tech! 🔎")

    st.markdown(
    """
    ### Our Mission
    At SmartDiag, we leverage AI to enhance medical diagnostic capabilities.We are driven by a vision where healthcare is empowered by cutting-edge technology, making diagnostics more accurate, accessible, and efficient for everyone.

    ### Who We Are
    Since our establishment in 2023, SmartDiag has been a pioneering force in the healthcare industry. With a commitment to innovation and excellence, we have consistently led the way in advancing diagnostic solutions through cutting-edge technology.

    ### Meet Our Team
    Our dedicated team brings a wealth of experience and skills to SmartDiag. Learn more about the individuals driving our mission.
    """
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image('os.path.join(os.path.dirname(__file__),"..", "pages", "Yash.jpg"', width=170, caption='Yash Shrivastava')

    with col2:
        st.image('os.path.join(os.path.dirname(__file__),"..", "pages", "Faisal.jpg"', width=170, caption='Rahimdad Faisal Safi')

    with col3:
        st.image('os.path.join(os.path.dirname(__file__),"..", "pages", "Sara.png"', width=170, caption='Sara Nourizadeh')

    with col4:
        st.image('os.path.join(os.path.dirname(__file__),"..", "pages", "Lore.jpg"', width=170, caption='Lorenzo Mosini')

    st.markdown(
    """

    ### Model Performance
    "We have implemented the VGG16 model as the cornerstone of our diagnostic approach, utilizing its robust capabilities in analyzing medical images.
    Trained on a dataset comprising 7000 chest X-ray images and 3500 Brain MRI images, our model has demonstrated commendable accuracy in predicting results.

    ### Ongoing Efforts and Future Goals
    "As we continually strive for excellence, our commitment to enhancing performance remains unwavering. We envision expanding our dataset in the near future, a crucial step towards refining our model's predictive accuracy.
    The pursuit of a larger and more diverse dataset aligns with our mission to deliver even more precise diagnostic outcomes.and aslo it's our goal to use more
    information about our patient like gender, historical medical information, or symptoms of disease to have more accurate
    diagnosis and be an assistant for doctor to reduce making mistake in doctor's diagnosis!

    ### More information about model
    User-Friendly Explanation:
    "For those interested in the technical details, the VGG16 model, known for its depth and effectiveness, serves as the backbone of our diagnostic process.
    Its architecture allows for intricate feature extraction, enabling accurate predictions from medical images.
    """

    )


    st.image('./bgs/model1.png', caption='Representation of the model we used')







# if __name__ == "__main__":
#     about()
