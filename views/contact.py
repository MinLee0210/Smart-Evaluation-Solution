import streamlit as st
from st_pages import add_page_title

# Add page title
add_page_title()

st.sidebar.write(
    """
    App created by AIO_Explorer
    """
)

# Main content
st.markdown(
    """
    ## Welcome to AIO_Explorer

    Our project is actively being developed, and we are always open to collaboration and questions. Feel free to reach out to us through the contact information provided below.

    ### Contact Us

    If you have any questions or would like to collaborate with us, please don't hesitate to contact us via email or LinkedIn.

    | **Team Member** | **Email** | **LinkedIn Profile** |
    |---|---|---|
    | **Lê Đức Minh** | [deutschlernen2303@gmail.com](mailto:deutschlernen2303@gmail.com) | [Minh Le's LinkedIn](https://www.linkedin.com/in/minh-le-duc-a62863172/) |
    | **Lê Nguyễn Đăng Khoa** | [khoale.maiu@gmail.com](mailto:khoale.maiu@gmail.com) | [Khoa Le's LinkedIn](https://www.linkedin.com/in/khoale-maiu/) |
    | **Trần Ngọc Đại** | [ngocdai101004@gmail.com](mailto:ngocdai101004@gmail.com) | [Ngoc Dai Tran's LinkedIn](https://www.linkedin.com/in/ngoc-dai-tran-621b62292/) |
    | **Minh Mẫn** | [phamminhman1312005@gmail.com](mailto:phamminhman1312005@gmail.com) | [Man Pham's LinkedIn](https://www.linkedin.com/in/m%E1%BA%ABn-ph%E1%BA%A1m-47b493311/) |

    We look forward to hearing from you and working together to innovate and transform the future of marketing.
    """
)
