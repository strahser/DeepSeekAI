import streamlit as st
from Components.HorizontalMenu import HorizontalMenu
from PagesData.AppAI import ChatUI
from PagesData.Home import display_home_content
from PagesData.SideBar import create_sidebar
from PagesData.UploadPage import upload_page

HOME = "Home"
UPLOAD = "Upload"
AI_CHAT = "AI Chat"
DOWNLOAD = "Download RVT, IFC, DWG converters"


def init_state():
    """Initializes session state variables."""
    if "excel_df" not in st.session_state:
        st.session_state["excel_df"] = None
    if "api_key" not in st.session_state:
        st.session_state["api_key"] = None


def main():
    def ai_chat_page():
        st.header("AI Chat Page")
        ui = ChatUI()
        ui.render()

    def create_downloads():
        pass

    # Set up the page configuration
    st.set_page_config(
        page_title="DDC Open AI",
        page_icon="🤖",
        layout="wide",
    )
    st.title("Chat with Revit and IFC")
    init_state()
    # Display the app title

    create_sidebar()

    # Define the pages for the menu
    pages = [
        {"title": "Home", "icon": "🏠", "function": display_home_content},
        {"title": "Upload", "icon": "⬆️", "function": upload_page},
        {"title": "AI Chat", "icon": "🤖", "function": ai_chat_page},
        # {"title": DOWNLOAD, "icon": "📥", "function": create_downloads},
    ]
    # Create an instance of HorizontalMenu and run it
    menu = HorizontalMenu(pages)

    menu.create_menu()
    menu.render_current_page()


if __name__ == "__main__":
    main()
