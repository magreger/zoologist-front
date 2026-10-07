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
"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?



1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""
url = 'http://localhost:8001/predict'

parameter = {'isalnd':island, 'bill_length': bill_length, 'bill_depth': bill_depth, 'flipper_length':flipper_length, 'body_mass': body_mass, 'sex': sex}

response = requests.get(url, params=parameter)

result = response.json()

#prediction = result['prediction']

print(result)
