import streamlit as st
from PagesData import UploadPage, AppAI
from PagesData.AppAI import  ChatUI
from PagesData.SideBar import create_sidebar


def init_state():
    """Initializes session state variables."""
    if "excel_df" not in st.session_state:
        st.session_state["excel_df"] = None

def main():
    init_state()
    st.title("Chat with Revit and IFC")
    UploadPage.upload_page()
    create_sidebar()
    ui = ChatUI()
    ui.render()

    # app = mt.MultiPage()
    # app.add("Upload 📁", UploadPage.upload_page)
    # if st.session_state["excel_df"] is not None:
    #     app.add("Chat with AI 🤖", AppAI.run)
    # app.run_radio()

main()