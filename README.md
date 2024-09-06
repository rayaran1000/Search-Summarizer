# Search Summarizer

![image](https://github.com/user-attachments/assets/e85d7d11-1cee-413b-962b-5f914e95023e)

## Project Overview

The **Search Summarizer** project is a tool designed to retrieve and summarize search results from DuckDuckGo. It leverages the **Llama 3** model to analyze search results and generate concise summaries, highlighting key topics, features, and important references. The application allows users to save both the raw and summarized search results in MongoDB for future use. 

## Key Features

1. **Real-time Search**:
Users can perform real-time searches on DuckDuckGo directly from the application. The results are fetched and displayed to the user.

2. **Summarization of Search Results**:
The **Llama 3** model is used to summarize the search results, providing key information on the topics searched, the main features of the results, and any important references.

3. **MongoDB Integration**:
Both raw search results and their corresponding summaries are saved in MongoDB collections (`search_results` and `search_summary`) for future reference.

4. **Flexible User Interaction**:
Users can perform a search, view the raw results, and then request a summary of those results for a concise understanding.

5. **DuckDuckGo Search Integration**:
The project uses **DuckDuckGo** as the search engine for fetching user queries, making it a privacy-centric search tool.## Workflow

1. **User Input**:
The user inputs a search query in the application through a text input field.

2. **Search Execution**:
When the user clicks the "Actual Search" button, the application uses the **DuckDuckGoSearchRun** tool to fetch search results.
The raw search results are displayed and saved in the MongoDB `search_results` collection.

3. **Summarization**:
   - The user can then click the "Summarized Search" button to invoke the **Llama 3** model and generate a summary of the search results.
   - The summary includes key topics, main features, and important references from the search.
   - The summarized results are saved in the `search_summary` collection in MongoDB.

4. **MongoDB Storage**:
Both the raw and summarized search results are stored in MongoDB, enabling users to retrieve previous searches and summaries later.
## Installation

To set up the Search summarizer locally, follow these steps:

### Clone the repository

```bash
   git clone <repository-url>
   cd search-summarizer
```

### Set up the environment

Create a .env file and add your MongoDB URI, Groq API key, and LangChain API key
```bash
    MONGODB_URI=<your-mongodb-uri>
    GROQ_API_KEY=<your-groq-api-key>
    LANGCHAIN_API_KEY=<your-langchain-api-key>
```

### Install the required dependencies
```bash
pip install -r requirements.txt
```

### Run the application
```bash
streamlit run app.py
```
    
