import streamlit as st
from PagesData import UploadPage, AppAI
from PagesData.AppAI import  ChatUI
from PagesData.Home import display_home_content
from PagesData.SideBar import create_sidebar
from streamlit_option_menu import option_menu

HOME = "Home"
UPLOAD = "Upload"
AI_CHAT = "AI Chat"
def init_state():
    """Initializes session state variables."""
    if "excel_df" not in st.session_state:
        st.session_state["excel_df"] = None
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = HOME


def set_current_page(page):
    """Set the current page."""
    st.session_state["current_page"] = page

def create_horizontal_menu():
    """
    Creates a horizontal menu using standard Streamlit elements.
    """
    # Get the current page from the session state
    current_page = st.session_state.get("current_page", HOME)

    # Create a horizontal menu using st.columns
    col1, col2, col3 = st.columns(3)

    # Add buttons for each page
    with col1:
        if st.button(f"🏠 {HOME}", key="home_button"):
            # Update the session state with the selected page and trigger a rerun
            st.session_state["current_page"] = HOME
            st.rerun()

    with col2:
        if st.button(f"⬆️ {UPLOAD}", key="upload_button"):
            # Update the session state with the selected page and trigger a rerun
            st.session_state["current_page"] = UPLOAD
            st.rerun()

    with col3:
        if st.button(f"🤖 {AI_CHAT}", key="ai_chat_button"):
            # Update the session state with the selected page and trigger a rerun
            st.session_state["current_page"] = AI_CHAT
            st.rerun()

def main():
    # Set up the page configuration
    st.set_page_config(
        page_title="DDC Open AI",
        page_icon="🤖",
        layout="wide",
    )
    # Display the app title
    st.title("Chat with Revit and IFC")

    create_sidebar()
    # Initialize the state
    init_state()

    # Create the horizontal menu
    create_horizontal_menu()

    # Handle page selection based on the current page stored in the session state
    selected_page = st.session_state.get("current_page", HOME)
    if selected_page == HOME:
        display_home_content()

    elif selected_page == UPLOAD:
        st.header("Upload Page")
        UploadPage.upload_page()

    elif selected_page == AI_CHAT:
        st.header("AI Chat Page")
        ui = ChatUI()
        ui.render()


    # app = mt.MultiPage()
    # app.add("Upload 📁", UploadPage.upload_page)
    # if st.session_state["excel_df"] is not None:
    #     app.add("Chat with AI 🤖", AppAI.run)
    # app.run_radio()


main()