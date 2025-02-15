
import streamlit as st
from Components.CustomButton import create_markdown_button_link
from Components.LogoImage import create_logo_base_64
from PagesData.Constants import GIT_HUB_LINK, LOGO_PATH, OPEN_AI_LINK, DDC_LINK, GIT_HUB_IMAGE


def create_sidebar():
    st.write("")
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
        create_markdown_button_link(GIT_HUB_LINK,GIT_HUB_IMAGE)
        st.markdown("---")
        st.markdown("## Additional tools")
        st.sidebar.caption(
            f"""
        🎬 [Video Tutorials](https://www.youtube.com/@datadrivenconstruction) for Using DDC Tools
        <br>
        📥 [Download](https://datadrivenconstruction.io/convertors/) RVT, IFC, DWG converters
        <br>
        🧮 [DDC Excel](https://datadrivenconstruction.io/ddc-excel-plugin-for-working-with-revit-ifc-and-dwg/) plugin
        <br>
        ⚡️ [Pipeline](https://datadrivenconstruction.io/pipeline-in-construction/) and ETL
                """
            , unsafe_allow_html=True
        )

        st.markdown("---")


