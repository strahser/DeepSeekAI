import streamlit as st
import openai

from PagesData.Utils import create_network_test


class ChatUI:
    def __init__(self):
        self.initialize_session_state()
        self.chat_processor = ChatProcessor()

    @staticmethod
    def initialize_session_state():
        """Initializes session state variables."""
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []
        if "api_key" not in st.session_state:
            st.session_state["api_key"] = ""
        if "excel_df" not in st.session_state:
            st.session_state["excel_df"] = None

    @staticmethod
    def display_chat_history():
        """Displays the chat history."""
        for role, content in st.session_state["chat_history"]:
            with st.chat_message(role):
                st.write(content, unsafe_allow_html=True)

    @staticmethod
    def _handle_api_key_input():
        """Handles API key input and updates session state."""
        api_key = st.text_input(
            "Enter your API Key:",
            type="password",
            key="api_key_input"
        )

    def _handle_user_input(self):
        """Handles user input processing and response generation."""
        df = st.session_state["excel_df"]
        prompt = st.chat_input("Ask questions about your data:")
        # check if it is first prompt
        if not any(role == "assistant" for role, _ in st.session_state["chat_history"]):
            # first message from AI
            welcome_message = "How can I assist you with your data? Feel free to ask anything!"
            st.session_state["chat_history"].append(("assistant", welcome_message))
        if prompt and self._validate_inputs(df):
            self._process_input(prompt, df)
            st.rerun()

    @staticmethod
    def _validate_inputs(df):
        """Validates required inputs before processing."""
        if not st.session_state["api_key"]:
            st.warning("Please enter your API key first.")
            return False
        if df is None:
            st.warning("Please upload an Excel file first.")
            return False
        return True

    def _process_input(self, prompt, df):
        """Processes user input and adds responses to chat history."""
        try:
            st.session_state["chat_history"].append(("user", prompt))
            with st.spinner("Running analysis..."):
                # response = create_network_test(df, prompt)
                response = self.chat_processor.process_request(
                    api_key=st.session_state["api_key"],
                    user_prompt=prompt,
                    df=df,
                    model="gpt"
                )
                st.session_state["chat_history"].append(("assistant", response))

        except Exception as e:
            error_msg = f"Error: {e}"
            st.session_state["chat_history"].append(("assistant", error_msg))

    def render(self):
        """Main method to render all UI components."""
        self.display_chat_history()
        self._handle_user_input()


class ChatProcessor:
    def __init__(self):
        self.html_template = """
        1. For tables: return **only** HTML using <table>, <tr>, <th>, <td> tags. Start immediately with <table>.
        2. For charts: return **only** SVG code with explicit dimensions. Start with <svg> tag. Include all necessary elements.
        3. Never add markdown, comments or text before/after HTML/SVG.
        4. For tables, use basic styling: border=1, cell padding=5.
        5. For SVG, set viewBox and preserve aspect ratio.
        6. Ensure all code is valid and can be directly rendered in streamlit.write().
        """

    def process_request(self, api_key, user_prompt, df, model):
        if "context_sent" not in st.session_state or not st.session_state["context_sent"]:
            # send context only one time
            st.info("Please wait while we initialize the data upload and set up the context for the chat session.")
            augmented_prompt = self._create_augmented_prompt(user_prompt, df)
            st.session_state["context_sent"] = True
        else:
            # send only user prompt
            augmented_prompt = f"User question: {user_prompt}\nYour Answer:"

        if model == "gpt":
            return self._get_openai_response(api_key, augmented_prompt)

    def _create_augmented_prompt(self, user_prompt, df):
        """Creates augmented prompt with DataFrame context."""
        return {
            "Your role": "You are an AI assistant helping to analyze pandas DataFrame. Follow these rules:",
            "instructions": self.html_template,
            "df_shape": df.shape,
            "df_columns": list(df.columns),
            "df_sample": df.head(5).to_markdown(),
            "df_description": df.describe().to_markdown(),
            "full Data Frame": df.to_markdown(),
            "User question": user_prompt,
            "Your Answer": ""
        }

    @staticmethod
    def _get_openai_response(api_key, prompt):
        """
        Generates a response from OpenAI's GPT-3.5-turbo model and checks connection/API key.

        Args:
            api_key: Your OpenAI API key.
            prompt: The prompt to send to the model.

        Returns:
            The content of the response from the model, or None if an error occurred.
        """
        try:
            openai.api_key = api_key
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": ""}
                ]
            )
            return completion.choices[0].message.content
        except openai.AuthenticationError as e:
            return f"Authentication Error: {e}. Please check your API key."
        except openai.APIConnectionError as e:
            return f"Connection Error: {e}. Please check your internet connection."
        except Exception as e:
            return f"An unexpected error occurred: {e}."
