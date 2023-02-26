import streamlit as st
import requests

st.title("Pun Generator")

user_input = st.text_input("Enter a word to generate puns:", "funny")

if st.button("Generate Puns"):
    url = "https://api.pungenerator.org/generate?word=" + user_input
    response = requests.get(url)
    if response.status_code == 200:
        puns = response.json()["puns"]
        st.write("Here are some puns based on your word:")
        for pun in puns:
            st.write(pun)
    else:
        st.write("Error generating puns. Please try again later.")
