import streamlit as st
from src.text_generator import generate_caption
from src.image_matcher import MemeMatcher

# Initialize meme matcher
matcher = MemeMatcher()

# Streamlit UI
st.title("🤖 AI Meme Generator")
user_input = st.text_input("Enter a topic for your meme:")

if user_input:
    # Generate caption
    prompt = f"Generate a funny caption about {user_input}"
    caption = generate_caption(prompt)
    st.subheader("Generated Caption:")
    st.write(caption)

    # Find matching image
    image_path = matcher.find_best_meme(caption)
    st.image(image_path, caption="Your AI-Generated Meme!")