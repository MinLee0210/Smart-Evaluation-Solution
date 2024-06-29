import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("X")
GROQ_API_KEY = os.getenv("X")

import streamlit as st

from controller.task import sec_pipeline
from src.tools import load_image

# ----- From Navigation bar ----- 
st.sidebar.write("")

# API_KEY = st.sidebar.text_input(
#     "Enter your HuggingFace API key",
#     help="Once you created you HuggingFace account, you can get your free API token in your settings page: https://huggingface.co/settings/tokens",
#     type="password",
# )

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
# st.markdown(
#     """
#     ### Give insights based your images. Hope you enjoy!
#     """
# )

st.header("Upload Image")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = load_image(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

end_result = sec_pipeline(image=image)
detected_obj = end_result['detected_obj']
context = end_result['image_context']
insight = end_result['insight']

st.subheader("Detected Object")
st.write(detected_obj)
st.divider()
st.subheader("Context")
st.write(context)
st.divider()


with st.expander("# Smart Analysis"):
    st.markdown(insight)