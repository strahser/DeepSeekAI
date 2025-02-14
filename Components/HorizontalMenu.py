import streamlit as st
from  typing import  Callable


class HorizontalMenu:
    """
    A class to create a horizontal menu with dynamic pages, icons and custom active state color.
    """

    def __init__(self, pages: list[dict]):
        """
        Initialize the HorizontalMenu with a list of pages.

        :param pages: List of dictionaries containing page details.
                      Each dictionary should have:
                      - "title": Title of the page (str)
                      - "icon": Icon for the page (str, optional)
                      - "function": Callable function to render the page content
        """
        self.pages = pages
        self._inject_custom_css()
        self.init_state()

    @staticmethod
    def _inject_custom_css():
        """Injects custom CSS for button styling."""
        st.markdown(
            f"""
            <style>
            /* Active button styling */
            div[data-testid="column"] > button[kind="primary"] {{
                background-color: #163969 !important;
                border-color: #163969 !important;
                color: white !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    def init_state(self):
        """
        Initializes the session state for the current page.
        """
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = self.pages[0]["title"]

    def create_menu(self):
        """
        Creates the horizontal menu using Streamlit columns and buttons with active state highlighting.
        """
        # Create columns dynamically based on the number of pages
        cols = st.columns(len(self.pages))

        # Add buttons for each page
        for i, page in enumerate(self.pages):
            title = page["title"]
            icon = page.get("icon", "")  # Optional icon
            key = f"{title.lower()}_button"
            current_page = st.session_state["current_page"]

            with cols[i]:
                # Display the button with an icon (if provided)
                if icon:
                    button_label = f"{icon} {title}"
                else:
                    button_label = title

                # Determine button type (primary for active page)
                button_type = "primary" if title == current_page else "secondary"

                if st.button(button_label,
                             key=key,
                             type=button_type,
                             use_container_width=True):
                    # Update the session state and trigger rerun
                    st.session_state["current_page"] = title
                    st.rerun()

    def render_current_page(self):
        """
        Renders the content of the currently selected page.
        """
        current_page = st.session_state.get("current_page")
        for page in self.pages:
            if page["title"] == current_page:
                page["function"]()
                break






