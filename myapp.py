import streamlit as st
import random

# list of possible sentence starters
starters = ["I love", "I hate", "I'm scared of", "I'm excited about", "I'm interested in"]

# list of possible sentence endings
endings = [
    "the color blue.",
    "pizza.",
    "going for walks.",
    "playing video games.",
    "learning new things.",
    "Never gonna give you up.",
]

def generate_text(seed_phrase):
    random.seed(seed_phrase)
    sentences = []
    # generate 5 random sentences
    for i in range(5):
        sentence = random.choice(starters) + " " + random.choice(endings)
        sentences.append(sentence)
    # concatenate the sentences and add the "Never gonna give you up" ending
    text = " ".join(sentences) + " " + random.choice(endings[-1:])
    return text

# streamlit app
st.title("Rick Roll Generator")

# get user input
seed_phrase = st.text_input("Enter a seed phrase to generate a Rick Roll paragraph:")

if seed_phrase:
    generated_text = generate_text(seed_phrase)
    st.write(generated_text)
