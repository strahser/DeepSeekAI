
import streamlit as st
def create_markdown_button_link(link_to_site:str, img_src:str):
    return st.markdown(
            f"""
            <a href="{link_to_site}" target="_blank">
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
                    <img src="{img_src}" 
                         alt="GitHub Logo" 
                         style="width: 16px; height: 16px; margin-right: 8px;" />
                    View the source code
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )