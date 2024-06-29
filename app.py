# import os
# from dotenv import load_dotenv

# import streamlit as st
# import google.generativeai as genai
# import numpy as np
# from PIL import Image
# import requests
# import json
# from transformers import pipeline
# from groq import Groq
# from src.prompt import object_detection

# load_dotenv()
# GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel('gemini-1.5-flash')


# def get_image_caption(image):
#     # caption_pipeline = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
#     # return caption_pipeline(image)[0]['generated_text']
#     # image = Image.open(image)
#     prompt = object_detection
#     response = model.generate_content(contents=[prompt, image]).text
#     return response


# def analyze_image_information(image_description):
#     prompt = f"""
#     Analyze the following image information and provide insights based on the criteria given below:

#     Image Description:
#     {image_description}

#     Criteria:
#     1. Brand Logos: Identify any brand logos mentioned in the description or OCR results.
#     2. Products: Mention any products such as beer kegs and bottles.
#     3. Customers: Describe the number of customers, their activities, and emotions.
#     4. Promotional Materials: Identify any posters, banners, and billboards.
#     5. Setup Context: Determine the scene context (e.g., bar, restaurant, grocery store, or supermarket).

#     Insights:
#     """

#     # Replace with your Groq API key

#     client = Groq(
#         # This is the default and can be omitted
#         api_key=GROQ_API_KEY,
#     )


#     data = {
#         "model": "llama3-8b-8192",
#         "messages": [{"role": "user", "content": prompt}]
#     }

#     chat_completion = client.chat.completions.create(**data)
#     return chat_completion.choices[0].message.content


# # Streamlit app
# st.set_page_config(layout="wide")
# st.title("Image Analysis App")

# # Create three columns with custom widths
# col1, col2, col3 = st.columns([1, 2, 2])

# with col1:
#     st.header("Upload Image")
#     uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# with col2:
#     st.header("OCR and Description")

#     if uploaded_file is not None:
#         # Load the image
#         image = Image.open(uploaded_file).convert("RGB")
#         st.image(image, caption='Uploaded Image', use_column_width=True)

#         # Get image caption
#         st.subheader("Image Description")
#         image_description = get_image_caption(image)
#         st.write(image_description)

#         # for text in ocr_texts:
#         #     st.write(text)

# with col3:
#     st.header("Analysis")

#     if uploaded_file is not None:
#         # Analyze image information
#         # ocr_results = ' '.join(ocr_texts)
#         analysis = analyze_image_information(image_description)
#         st.write(analysis)

import streamlit as st
from st_pages import Page, show_pages


st.set_page_config(
    layout="centered", page_title="Doco-DocumentCompressor", page_icon="static/doco_logo.jpg"
)

show_pages(
    [
        Page("views/home.py", "🏠 Home"), 
        Page("views/main.py", "🔬 Main Page"), 
        Page("views/about.py", "🔎 Explorers Story"), 
        Page("views/contact.py", "📨 Contact Us")
    ]
)