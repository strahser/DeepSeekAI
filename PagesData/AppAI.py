import time
import random

import streamlit as st
from gigachat import GigaChat

from PagesData.Utils import neural_network_responses


def initialize_session_state():
    """Initializes session state variables."""
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    if "api_key" not in st.session_state:
        st.session_state["api_key"] = ""

def display_chat_history():
    """Displays the chat history."""
    for role, content in st.session_state["chat_history"]:
        with st.chat_message(role):
            st.write(content, unsafe_allow_html=True)


def process_user_input(user_prompt, df): # Added df as argument
    """Processes user input using GigaChat (with DataFrame) and updates the chat history."""
    api_key = st.session_state.get("api_key")
    if not api_key:
        st.warning("Please enter your API key first.")
        return

    if df is None:
        st.warning("Please upload an Excel file first.")
        return

    try:
        #Prepare the prompt pay attention that we provide all data frame!! not df.head()
        augmented_prompt = (
            f"""You are an AI assistant helping to analyze pandas DataFrame. Follow these rules:
        1. For tables: return **only** HTML using <table>, <tr>, <th>, <td> tags. Start immediately with <table>.
        2. For charts: return **only** SVG code with explicit dimensions. Start with <svg> tag. Include all necessary elements.
        3. Never add markdown, comments or text before/after HTML/SVG.
        4. For tables, use basic styling: border=1, cell padding=5.
        5. For SVG, set viewBox and preserve aspect ratio.
        6. Ensure that all HTML or SVG code is valid and can be directly rendered by tools like Streamlit with method st.write(content, unsafe_allow_html=True)

        DataFrame sample (shape {df.shape}):
        {df.to_markdown()}

        User question: {user_prompt}

        Your Answer:"""
        )
        # Add a spinner
        with st.spinner("Running analysis..."):
            _create_gigachat_response(api_key, augmented_prompt, user_prompt)

    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.session_state["chat_history"].append(("user", user_prompt))
        st.session_state["chat_history"].append(("assistant", f"Error: {e}"))


def _network_test(df, user_prompt):
    time.sleep(random.uniform(1, 4))
    st.session_state["chat_history"].append(("user", user_prompt))
    try:
        selected_function = neural_network_responses.get(user_prompt)
        result = selected_function(df)
        st.session_state["chat_history"].append(("assistant", result))
    except Exception as e:
        st.session_state["chat_history"].append(("assistant", e))



def _create_gigachat_response(api_key, augmented_prompt, user_prompt):
    with GigaChat(credentials=api_key, verify_ssl_certs=False) as giga:
        response = giga.chat(augmented_prompt)
        response_text = response.choices[0].message.content
        st.session_state["chat_history"].append(("user", user_prompt))
        st.session_state["chat_history"].append(("assistant", response_text))


def chat_with_ai_tab():
    st.title("Chat with Excel Data")

    # 0. Init
    initialize_session_state()

    # 1. API Key Input
    api_key = st.text_input("Enter your  API Key:", type="password", key="api_key_input")

    # Update API key in session state if changed
    if api_key and api_key != st.session_state["api_key"]:
        st.session_state["api_key"] = api_key
        st.success("API key updated.")

    # 3. Display Chat History
    display_chat_history()

    # 4. Chat Input and Response

    df = st.session_state.get("excel_df") # Get DataFrame from session state


    if st.session_state.get("api_key") and df is not None and (prompt := st.chat_input("Ask questions about your data:")):
        process_user_input(prompt, df)  # Pass the DataFrame to process_user_input
        st.rerun()


# Example usage (assuming this script is the main app)
if __name__ == "__main__":


    chat_with_ai_tab()