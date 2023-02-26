import streamlit as st
import nltk
nltk.download('punkt')
import random

# Define the seed text and the song lyrics
seed_text = "Enter your seed text here"
song_lyrics = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you"]

# Define the Streamlit app
st.title("Text Generator")
st.write("Enter a seed phrase below and click the button to generate a paragraph that ends with the lyrics of 'Never Gonna Give You Up'.")

# Get the seed text from the user
seed_text = st.text_input("Seed phrase", seed_text)

# Generate the text
if st.button("Generate"):
    # Tokenize the seed text
    seed_tokens = nltk.word_tokenize(seed_text)
    # Generate a random number of sentences (between 1 and 5) to add to the seed text
    num_sentences = random.randint(1, 5)
    for i in range(num_sentences):
        # Use the NLTK library to generate the next word based on the previous words
        cfd = nltk.ConditionalFreqDist(nltk.bigrams(seed_tokens))
        next_word = cfd[seed_tokens[-1]].max()
        seed_tokens.append(next_word)
    # Combine the tokens into a single string and capitalize the first letter
    paragraph = " ".join(seed_tokens)
    paragraph = paragraph[0].upper() + paragraph[1:]
    # Add the song lyrics at the end
    paragraph += "\n" + "\n".join(song_lyrics)
    st.write(paragraph)
