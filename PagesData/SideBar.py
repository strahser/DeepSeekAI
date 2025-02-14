import base64
import os
import streamlit as st

from PagesData.Constants import GIT_HUB_LINK, LOGO_PATH, OPEN_AI_LINK, DDC_LINK


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
        create_logo_base_64(LOGO_PATH,DDC_LINK, width="500")
        st.markdown(
            "## How to use\n"
            f"1. 🔑 Enter your [OpenAI API key]({OPEN_AI_LINK})\n"  # noqa: E501
            "2. 📄 Upload a RVT, IFC or XLSX \n"
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
        st.markdown("## Additional tools")
        st.caption(
            """We can add here links for another tools, like list of content"""
            # f"""
            # Our tool converts your data into a DataFrame format, facilitating seamless interaction with any Large
            # Language Model (LLM). By running the chat application on your local machine, you maintain complete control
            # over both your data and the processing workflow. This ensures enhanced privacy and security,
            # as all operations are performed locally without transmitting information externally.
            # For more detailed information on how ChatGPT and other LLMs can automate data processes,
            # please visit: [LLM with CAD Data]({DDC_LINK})
            # """
        )
        st.markdown("---")


