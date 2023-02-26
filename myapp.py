import random
import streamlit as st

# Define a list of jokes
jokes = [    "Why did the tomato turn red? Because it saw the salad dressing!",    "Why did the scarecrow win an award? Because he was outstanding in his field!",    "Why do cows wear bells? Because their horns don't work!",    "Why did the chicken cross the playground? To get to the other slide!",    "Why don't scientists trust atoms? Because they make up everything!",    "What do you call a lazy kangaroo? A pouch potato!",]

# Define the Streamlit app
def main():
    st.title("Random Joke Generator")
    st.write("Click the button below to generate a random joke!")
    if st.button("Generate Joke"):
        joke = random.choice(jokes)
        st.write(joke)

if __name__ == "__main__":
    main()
