import streamlit as st
import requests

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)


island = st.text_input('the location where the penguin lives','Biscoe, Dream or Torgersen')

bill_length = st.number_input('bill length (in mm)')
bill_depth = st.number_input('bill depth (in mm)')
flipper_length = st.number_input('flipper length (in mm)')
body_mass = st.number_input('body_mass (in g)')

sex = st.text_input('sex','Male or Female')


url = st.secrets['API_URL']
#'http://localhost:8001/predict'

if st.button("Predict"):
    parameter = {'island':island,
                 'bill_length_mm': bill_length,
                 'bill_depth_mm': bill_depth,
                 'flipper_length_mm':flipper_length,
                 'body_mass_g': body_mass,
                 'sex': sex}

    response = requests.get(url, params=parameter)

    result = response.json()

    #prediction = result['prediction']

    st.write('Prediction:', result)
