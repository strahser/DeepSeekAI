# Data Analysis Chatbot README

This project is a Streamlit-based application that allows users to upload an Excel file and then chat with an AI assistant to analyze the data within that file. The AI assistant is powered by a "neural network" that can perform various data analysis tasks based on user prompts.

**Repository Link:** [https://github.com/strahser/DeepSeekAI.git](https://github.com/strahser/DeepSeekAI.git)

## Key Features

1.  Convert CAD (BIM) formats RVT, IFC, into a DataFrame for analysis.
2.  Either load your data in XLSX that came from the DDC conversion tools or load any XLSX and CSV you are working with in the project.
3.  Interact with the data through natural language queries via the AI Chat interface.

## Requirements

The following Python packages are required to run this application:

*   matplotlib
*   streamlit
*   openpyxl
*   seaborn
*   openai
*   tabulate
*   pandas

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/strahser/DeepSeekAI.git
    cd DeepSeekAI
    ```

2.  **Install dependencies:**

    This project uses a `requirements.txt` file to manage dependencies. You can install all the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, you can install the dependencies individually:

    ```bash
    pip install streamlit openpyxl matplotlib seaborn openai tabulate pandas
    ```

## Setup and Usage

1.  **Install Dependencies:** Make sure you have installed all the required Python packages as described in the "Installation" section above.

2.  **API Key (Optional):** If you want to use Open AI integration, obtain an API key from OpenAI's website. You'll need to set this up within the Streamlit application's user interface (usually in a configuration section or chat settings).

3.  **Run the Application:** Save the main code as a Python file (e.g., `app.py`) and run it using Streamlit:

    ```bash
    streamlit run app.py
    ```

    This will open the application in your web browser.

4.  **Upload an Excel File:** In the "Upload" page (if applicable in your application), upload your Excel file using the file uploader.

5.  **Chat with AI:** Navigate to the "Chat with AI" page (if applicable). Enter your API key (if required) and begin asking questions about your data in the chat input.

## Code Structure

[*(Optional:  Add a brief overview of the main Python files and their purpose.  For example:)*]
[*(Example:  `app.py` contains the main Streamlit application logic.  `data_processing.py` contains functions for data cleaning and transformation.)*]

This README provides a comprehensive overview of the Data Analysis Chatbot project, including its features, setup instructions, code structure, limitations, and potential future enhancements.