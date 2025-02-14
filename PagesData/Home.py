import streamlit as st

from PagesData.Constants import DDC_LINK


def display_home_content():
    """
    Displays the content of the Home page with a structured and styled description.
    """
    st.markdown(f"""
    ## About This App

    Our tool helps you convert your data into a **DataFrame** format, enabling seamless interaction with any **Large Language Model (LLM)**. By running the chat application on your local machine, you retain **full control** over both your data and the processing workflow.

    ### Key Features:
    - **Privacy & Security**: All operations are performed locally without transmitting your data externally.
    - **Customizable Workflow**: Process your data using the power of LLMs while maintaining complete control.
    - **Efficient Automation**: Automate complex data processes with ease using advanced language models.

    ### How It Works:
    1. Upload your data in supported formats (e.g., Excel, CSV).
    2. Convert it into a DataFrame for analysis.
    3. Interact with the data through natural language queries via the AI Chat interface.

    For more detailed information on how **ChatGPT** and other LLMs can automate data processes, visit our [LLM with CAD Data]({DDC_LINK}) guide.

    ---

    #### Why Choose Us?
    - **Local Processing**: Your data never leaves your machine.
    - **User-Friendly Interface**: Easily interact with your data using intuitive controls.
    - **Powerful Integration**: Leverage the capabilities of cutting-edge LLMs to enhance your workflows.

    Start exploring the possibilities today!
    """, unsafe_allow_html=False)