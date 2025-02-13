import os

import streamlit as st
GIT_HUB_LINK = "https://github.com/strahser/DeepSeekAI"
OPEN_AI_LINK ="https://platform.openai.com/api-keys."
DDC_LINK = "https://datadrivenconstruction.io/chatgpt-and-llm/"
def display_image(image_path, alt_text="Image", width=None, height=None):
    """Displays an image.

    Args:
        image_path: Path to the image file (e.g., "logo.png" or "logo.jpg").
        alt_text: Alternative text for the image.
        width: Width of the image in pixels (optional).
        height: Height of the image in pixels (optional).
    """
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
            <img src=""
                 alt="{alt_text}"
                 style="{style}"/>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"An error occurred: {e}")

def create_markdown_button_link():
    return st.markdown(
            f"""
            <a href="{GIT_HUB_LINK}" target="_blank">
                <button style="
                    background-color: black;
                    color: white;
                    padding: 5px 15px; 
                    border: none;
                    border-radius: 5px; /* Сlightly smaller rounding */
                    font-size: 14px; 
                    cursor: pointer;
                    height: 30px; 
                    width: 150px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                ">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" 
                         alt="GitHub Logo" 
                         style="width: 16px; height: 16px; margin-right: 8px;" />
                    View the source code
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )
def create_sidebar():

    with st.sidebar:
        LOGO_PATH = "resources/DdcLabel.jpg"
        st.logo(LOGO_PATH,size="large")

        st.markdown(
            "## How to use\n"
            f"1. 🔑Enter your [OpenAI API key]({OPEN_AI_LINK}) below\n"  # noqa: E501
            "2. 📄 Upload a RVT or IFC \n"
            "3. 💬 Ask a question to the data\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help=f"You can get your API key from  {OPEN_AI_LINK}",  # noqa: E501
        )

        if api_key_input and api_key_input != st.session_state["api_key"]:
            st.session_state["api_key"] = api_key_input
            st.success("✅ API key already provided.")
        st.markdown(f"[Get an OpenAI API key]({OPEN_AI_LINK})")
        create_markdown_button_link()
        st.markdown("---")
        st.markdown("## About this app")
        st.markdown(
                    f"""Our tool converts your data into a DataFrame format, facilitating seamless interaction with any Large 
                    Language Model (LLM). By running the chat application on your local machine, you maintain complete control 
                    over both your data and the processing workflow. This ensures enhanced privacy and security, 
                    as all operations are performed locally without transmitting information externally.
                    For more detailed information on how ChatGPT and other LLMs can automate data processes, 
                    please visit: [LLM with CAD Data]({DDC_LINK})
                    """
        )
        st.markdown("---")