# views/home.py

import streamlit as st

st.title("SES - Smart Evaluation Solution ")

# Adding an image
st.image("./docs/static/flow.png",
         caption="Production Flow", use_column_width=True)


st.markdown("""
Our AI solution streamlines the analysis of promotional activities at retail environments by leveraging cutting-edge OCR and LLM technologies. Key features include:

- **Brand Logo Detection**: Automatically spot Heineken, Tiger, Bia Viet, and other logos.
- **Product Identification**: Recognize beer kegs and bottles.
- **Consumer Analysis**: Gauge quantity, activities, and emotions.
- **Promotional Material Recognition**: Identify posters, banners, and billboards.
- **Context Decoding**: Determine the scene—bar, restaurant, grocery store, or supermarket.

This comprehensive system ensures accurate, real-time insights, empowering Heineken to optimize branding strategies and enhance customer experiences.
""")
