import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize, sent_tokenize

seed_phrase = st.text_input("Enter a seed phrase:", "I love")
generated_text = ""

if seed_phrase:
    # Tokenize seed phrase
    seed_tokens = word_tokenize(seed_phrase)

    # Generate text
    generated_text = seed_phrase + " "
    for i in range(5):
        # Get the last word of the generated text
        last_word = generated_text.split()[-1]
        
        # Generate the next word based on the last word using a bigram model
        cfd = nltk.ConditionalFreqDist(nltk.bigrams(word_tokenize(generated_text)))
        if last_word in cfd:
            next_word = cfd[last_word].max()
        else:
            next_word = ""

        generated_text += next_word + " "

    # End the generated text with "Never Gonna Give You Up"
    generated_text += "Never gonna give you up."

st.write(generated_text)
