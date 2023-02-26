import streamlit as st
import markovify

# Define the function to generate text using Markov Chain
def generate_text(text_input):
    text_model = markovify.Text(text_input, state_size=2)
    generated_text = text_model.make_sentence()
    return generated_text

# Define the Streamlit app
def app():
    st.title("Rick Roll Generator")
    st.write("Enter a seed phrase to generate text:")
    
    # Input for the seed phrase
    seed_phrase = st.text_input("Seed Phrase:")
    
    # Generate text using the seed phrase
    if st.button("Generate"):
        if seed_phrase:
            generated_text = generate_text(seed_phrase)
            if generated_text:
                st.write(generated_text.capitalize() + ". Never gonna give you up.")
            else:
                st.write("Sorry, could not generate text. Please try a different seed phrase.")
        else:
            st.write("Please enter a seed phrase to generate text.")
