import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("X")
GROQ_API_KEY = os.getenv("X")

import streamlit as st

from controller.tasks import get_image_captioning, analyze_image_information
from src.agent.gemini import GeminiAgent
from src.agent.groq import GroqAgent
from src.tools import get_image

# ----- From Navigation bar ----- 
st.sidebar.write("")

# API_KEY = st.sidebar.text_input(
#     "Enter your HuggingFace API key",
#     help="Once you created you HuggingFace account, you can get your free API token in your settings page: https://huggingface.co/settings/tokens",
#     type="password",
# )

if GEMINI_API_KEY: 
    ...

else: 
    ...

if GROQ_API_KEY: 
    ... 
else: 
    ...

vision_model = GeminiAgent(api_key=GEMINI_API_KEY)
language_model = GroqAgent(api_key=GROQ_API_KEY)

st.sidebar.write(
    """
    App created by AIO_Explorer
    """
)

# ----- From Main side -----
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(
        "static/angelhack.webp",
        width=100,
    )
st.caption("")
st.title("AIO_Explorer")

if not "valid_inputs_received" in st.session_state:
    st.session_state["valid_inputs_received"] = False

st.write("")
st.markdown(
    """
    ### Give insights based your images. Hope you enjoy!
    """
)

st.header("Upload Image")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])


with st.expander("## Image Description"):
    if uploaded_file is not None:
        # Load the image
        image = get_image(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Get image caption
        st.subheader("Image Description")
        image_description = get_image_captioning(vision_model, image)
        st.write(image_description.text)

with st.expander("## Smart Analysis"):
    if uploaded_file is not None:
        analysis = analyze_image_information(language_model, image_description)
        st.write(analysis)