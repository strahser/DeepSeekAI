import streamlit as st
import multipage_streamlit as mt
from PagesData import UploadPage, AppAI

def init_state():
    """Initializes session state variables."""
    if "excel_df" not in st.session_state:
        st.session_state["excel_df"] = None
def main():
    init_state()
    app = mt.MultiPage()
    app.add("Upload 📁", UploadPage.upload_page)
    if st.session_state["excel_df"] is not None:
        app.add("Chat with AI 🤖", AppAI.chat_with_ai_tab)
    app.run_radio()

main()