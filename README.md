# Data Analysis Chatbot README

This project is a Streamlit-based application that allows users to upload an Excel file and then chat with an AI assistant to analyze the data within that file. The AI assistant is powered by a "neural network" that can perform various data analysis tasks based on user prompts.

## Key Features

*   **Excel File Upload:** Users can upload an Excel file (.xlsx) to be analyzed.
*   **API Key Integration:**  Users can provide their API key for GigaChat, a large language model, to enable more sophisticated data analysis.
*   **Chat Interface:**  A chat interface allows users to ask questions about the uploaded data.*   
*   **Chart Generation:** The application can generate and display various charts (e.g., bar charts) based on user prompts.*  
*   **Multi-Page Interface:** The application is structured as a multi-page Streamlit app, allowing for a cleaner user experience by separating the upload and chat functionalities.
*   

## Requirements

*   Python 3.6+
*   Streamlit
*   openpyxl
*   matplotlib
*   seaborn (might be needed for some chart types)
*   multipage-streamlit (for multi-page app structure)
*   gigachat (if you intend to integrate with the Gigachat API)

To install these dependencies, run:

```bash
pip install streamlit openpyxl matplotlib seaborn multipage-streamlit gigachat

markdown
Setup and Usage
Install Dependencies: Make sure you have installed all the required Python packages.

API Key (Optional): If you want to use GigaChat integration, obtain an API key from GigaChat’s website.

Run the Application: Save the provided code as a Python file (e.g., app.py) and run it using Streamlit:

streamlit run app.py

bash
This will open the application in your web browser.

Upload an Excel File: In the “Upload” page, upload your Excel file using the file uploader.

Chat with AI: Navigate to the “Chat with AI” page. Enter your API key (if desired) and begin asking questions about your data in the chat input.


Code Structure

This README provides a comprehensive overview of the Data Analysis Chatbot project, including its features, setup instructions, code structure, limitations, and potential future enhancements. “`