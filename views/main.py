from src.tools import load_image, get_image
from controller.task import ses_pipeline, get_annotate_image
import streamlit as st
import os
from dotenv import load_dotenv
from matplotlib import pyplot as plt

load_dotenv()

GEMINI_API_KEY = os.getenv("X")
GROQ_API_KEY = os.getenv("X")


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
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image(
        "./docs/static/angelhack.webp",
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
uploaded_file = st.file_uploader(
    "Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = get_image(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    with st.status("Please wait ..."):

        end_result = ses_pipeline(image=image)

        detections = end_result['detections']
        detected_obj = end_result['detected_obj']
        image_ocr = end_result['image_ocr']
        context = end_result['image_context']
        insight = end_result['insight'].text
        # insight = end_result['insight']

        # annotated_img = get_annotate_image(detections)
        # st.image(annotated_img, caption='Annotated Image', use_column_width=True)
        st.subheader("Context")
        st.write(context)
        st.divider()
        st.subheader("OCR")
        st.write(image_ocr)
        st.title('Beer Popularity Bar Chart')

        # Extract keys and values
        labels = list(image_ocr.keys())
        values = list(image_ocr.values())

        # Create a bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(labels, values, color='skyblue')

        # Add title and labels
        ax.set_title('Beer Popularity')
        ax.set_xlabel('Beer Brands')
        ax.set_ylabel('Counts')

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')

        # Add grid lines for better readability
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Display the plot in Streamlit
        st.pyplot(fig)

        st.divider()

    with st.expander("# Smart Analysis"):
        st.markdown(insight)
