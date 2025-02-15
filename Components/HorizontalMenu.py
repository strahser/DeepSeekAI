import streamlit as st
from  typing import  Callable


class HorizontalMenu:
    """
    Класс для горизонтального меню с фиксированным цветом активной кнопки
    """

    def __init__(self, pages: list[dict], active_color: str = "#163969"):
        self.pages = pages
        self.active_color = active_color
        self._inject_custom_css()
        self.init_state()

    def _inject_custom_css(self):
        st.markdown(f"""
            <style>
            /* Базовые стили для всех кнопок */
            div.stButton > button {{
                transition: all 0.3s ease !important;
                border: 1px solid {self.active_color} !important;
                background-color: #F0F2F6 !important;
                color: black !important;
            }}

            /* Стили для активной кнопки */
            div.stButton > button:focus:not(:active),
            div.stButton > button[data-active="true"] {{
                background-color: {self.active_color} !important;
                color: white !important;
            }}

            /* Отключаем эффект нажатия */
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

                # Создаем кнопку с кастомным атрибутом
                clicked = st.button(
                    f"{page.get('icon', '')} {title}",
                    key=f"btn_{title}",
                    use_container_width=True
                )

                # Обновляем состояние при клике
                if clicked:
                    st.session_state.current_page = title
                    st.rerun()

                # Добавляем кастомный атрибут через HTML
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






