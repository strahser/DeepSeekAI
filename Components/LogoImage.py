import base64
import os
import streamlit as st
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def create_logo_base_64(logo_path, logo_link, width="100px", height="auto"):
    logo_base64 = get_image_base64(logo_path)
    clickable_image_html = f"""
    <a href="{logo_link}" target="_blank">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo" style="width:{width}; height:{height};">
    </a>
    """
    st.markdown(clickable_image_html, unsafe_allow_html=True)

def display_image(image_path, alt_text="Image", width=None, height=None):
    try:
        # Check if the file exists
        if not os.path.exists(image_path):
            st.error(f"Error: Image file not found at {image_path}")
            return

        # Construct the style string
        style = ""
        if width:
            style += f"width: {width}px;"
        if height:
            style += f"height: {height}px;"

        st.markdown(
            f"""
            <img src="{image_path}"
                 alt="{alt_text}"
                 style="{style}"/>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"An error occurred: {e}")

