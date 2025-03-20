import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("API key not found. Please check your .env file.")

# Initialize Gemini Client
client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_image(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp-image-generation",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=['Text', 'Image']
        )
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            return image
    return None

# Streamlit UI
st.title("Text-to-Image Generator")
st.write("Enter a prompt and generate an AI-powered image.")

user_input = st.text_area("Enter your image description:", "A futuristic city with flying cars")

if st.button("Generate Image"):
    if user_input:
        with st.spinner("Generating image..."):
            generated_image = generate_image(user_input)
            if generated_image:
                st.image(generated_image, caption="Generated Image", use_column_width=True)
            else:
                st.error("Failed to generate image. Try again with a different prompt.")
    else:
        st.warning("Please enter a prompt before generating.")
