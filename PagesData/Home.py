import streamlit as st

from PagesData.Constants import DDC_LINK


def display_home_content():
    """
    Displays the content of the Home page with a structured and styled description.
    """

    st.markdown(f"""
    ## About This App

    Our DDC LLM tool helps you convert CAD (BIM) data into a **DataFrame** format, enabling seamless interaction with any **Large Language Model (LLM)**.  
    By running the chat application on your local machine, you retain **full control** over both your data and the processing workflow.

    ### Key Features:
    - **Privacy & Security**: All operations are performed locally without transmitting your data externally.
    - **Customizable Workflow**: Process your data using the power of LLMs while maintaining complete control.
    - **Efficient Automation**: Automate complex data processes with ease using advanced language models.

    ### How It Works:
    1.  Convert CAD (BIM) formats RVT, IFC, into a DataFrame for analysis.
    2.  Either load your data in XLSX that came from the DDC conversion tools or load any XLSX and CSV you are working with in the project.
    3.  Interact with the data through natural language queries via the AI Chat interface.

    For more detailed information on how **ChatGPT** and other LLMs can automate data processes, visit our [LLM with CAD Data]({DDC_LINK}) guide.

    ### What are Dataframe and structured formats for?
    Structured data, organized in columns and rows, has become the backbone of modern storage and analysis systems due to its orderliness and ease of processing.  For example, only one Pandas library that processes DataFrame data is loaded about 12 million times a day. Due to its popularity and ease of use, DataFrame has become the main format for data processing and automation in LLM tools.

    ---

    #### Why Choose Us?
    - Working with CAD (BIM) data offline and without starting CAD (BIM) tools.
    - **Local Processing**: Your data never leaves your machine.
    - **User-Friendly Interface**: Easily interact with your data using intuitive controls.
    - **Powerful Integration**: Leverage the capabilities of cutting-edge LLMs to enhance your workflows.

    """, unsafe_allow_html=False)
