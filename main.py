import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')
import pybase64

st.set_page_config(page_title="Diabetes Prediction", page_icon="",layout="wide", initial_sidebar_state="expanded")
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return pybase64.b64encode(data).decode()
img = get_img_as_base64("bg1.jpg")
st.markdown(
    """
    <style>
    .main {
        padding: 0rem 0rem;
    }
    .sidebar .sidebar-content {
        width: 300px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Diabetes Prediction")


menu = option_menu(menu_title='',options=['Home','Contact'],orientation='horizontal',
        default_index=0, icons=['house','envelope'])
with open('finalized_model.pkl', 'rb') as model_file:
    finalized_model = pickle.load(model_file)
if menu == 'Home':
    # st.markdown('__<p style="font-family: verdana; text-align:left; font-size: 15px; color: #FAA026">'
    #             'Our web application provides an interactive platform to predict Diabetes.</P>__', unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input(label='Pregnancies', min_value=0, max_value=20)
        Glucose = st.number_input(label='Glucose', min_value=0.0, max_value=200.0)
        BP = st.number_input(label='Blood Pressure', min_value=0.0, max_value=200.0)
        ST = st.number_input(label='SkinThickness', min_value=0.0, max_value=100.0)

    with col2:
        Insulin = st.number_input(label='Insulin', min_value=0.0, max_value=1000.0)
        BMI = st.number_input(label='Body Mass Index(BMI)', min_value=0.0, max_value=100.0)
        DPF = st.number_input(label='DiabetesPedigreeFunction', min_value=0.0, max_value=3.0)
        Age = st.number_input(label='Age', min_value=18, max_value=100)

    predict = st.button(label='Predict')
    new_datapoint = [Pregnancies, Glucose, BP, ST, Insulin,BMI, DPF, Age]

    #loading pickled datapoints


    if predict:
        new_data = np.array(new_datapoint)
        # Reshape the input data to be 2D
        new_data = new_data.reshape(1, -1)
        predictions = finalized_model.predict(new_data)
        # 'predictions' will contain the predicted class (0 or 1) based on your XGBoost model
        print(predictions)
        if predictions[0] == 1:
            st.error("The likelihood of Diabetes is high.")

        else:
            st.success("The likelihood of Diabetes is less.")
elif menu == 'Contact':
    st.markdown('__<p style="text-align:left; font-size: 20px; color: #FAA026">Applications and Packages Used:</P>__',
                unsafe_allow_html=True)
    st.write("  * Python")
    st.write("  * Scikit-Learn")
    st.write("  * Pandas")
    st.write("  * Numpy")
    st.write("  * Pickle")
    st.write("  * Streamlit")
    st.write("  * Github")
    st.markdown(
        '__<p style="text-align:left; font-size: 20px; color: #FAA026">For feedback/suggestion, connect with me on</P>__',
        unsafe_allow_html=True)
    st.subheader("LinkedIn")
    st.write("https://www.linkedin.com/in/selvamani-a-795580266/")
    st.subheader("Email ID")
    st.write("selvamani.ind@gmail.com")
    st.subheader("Github")
    st.write("https://github.com/selvamani1992")