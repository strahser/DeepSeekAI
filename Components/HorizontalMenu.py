import streamlit as st


class HorizontalMenu:
    """
    Class for a horizontal menu with a fixed active button color
    """

    def __init__(self, pages: list[dict], active_color: str = "#163969"):
        self.pages = pages
        self.active_color = active_color
        self._inject_custom_css()
        self.init_state()

    def _inject_custom_css(self):
        st.markdown(f"""
            <style>
            /* Base styles for all buttons */
            div.stButton > button {{
                transition: all 0.3s ease !important;
                border: 1px solid {self.active_color} !important;
                background-color: #F0F2F6 !important;
                color: black !important;
            }}

            /* Styles for the active button */
            div.stButton > button:focus:not(:active),
            div.stButton > button[data-active="true"] {{
                background-color: {self.active_color} !important;
                color: white !important;
            }}

            /* Disable the click effect */
            div.stButton > button:active {{
                transform: none !important;
            }}
            </style>
            """,
                    unsafe_allow_html=True
                    )

    def init_state(self):
        if "current_page" not in st.session_state:
            st.session_state.current_page = self.pages[0]['title']

    def create_menu(self):
        cols = st.columns(len(self.pages))
        for idx, page in enumerate(self.pages):
            with cols[idx]:
                title = page['title']
                is_active = st.session_state.current_page == title

                # Create a button with a custom attribute
                clicked = st.button(
                    f"{page.get('icon', '')} {title}",
                    key=f"btn_{title}",
                    use_container_width=True
                )

                # Update state on click
                if clicked:
                    st.session_state.current_page = title
                    st.rerun()

                # Add a custom attribute via HTML
                if is_active:
                    st.markdown(
                        f"<script>document.querySelector('button[data-testid=\"baseButton-secondary\"]')"
                        f".setAttribute('data-active', 'true')</script>",
                        unsafe_allow_html=True
                    )

    def render_current_page(self):
        for page in self.pages:
            if page['title'] == st.session_state.current_page:
                page['function']()
                break
