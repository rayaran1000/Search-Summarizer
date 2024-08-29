import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# MongoDB Connection
MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    st.error("MONGODB_URI not set in environment variables.")
    st.stop()

client = MongoClient(MONGODB_URI)
db = client["search_summarization"]
search_collection = db["search_results"]
summary_collection = db["search_summary"]

# Load API keys
groq_api_key = os.environ.get('GROQ_API_KEY')
if not groq_api_key:
    st.error("Groq API key is missing. Please set the GROQ_API_KEY environment variable.")
    st.stop()

langchain_api_key = os.environ.get('LANGCHAIN_API_KEY')
if not langchain_api_key:
    st.error("LangChain API key is missing. Please set the LANGCHAIN_API_KEY environment variable.")
    st.stop()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

# Load the LLM (Llama3 model)
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")

# Chat prompt template for summarization
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a highly capable AI language model, skilled at understanding and summarizing complex user search results. You can extract key information, identify main ideas, and provide concise summaries."),
    ("human",
     """I have uploaded the search textual results of the question {input} provided by the user. 
    Please summarize the user search results in the following format:
    1. Key topics and information about the topics
    2. The key features of the topics searched by the user
    3. Any important references about the topic searched by the user
    The textual content of the user search result is here: {context}
    """)
])

summarization_chain = LLMChain(llm=llm, prompt=summary_prompt)
search = DuckDuckGoSearchRun()

st.title("Search Results Summarizer")

user_query = st.text_input('What are you searching for?')

if user_query:
    if st.button("Actual Search"):
        try:
            search_results = search.invoke(user_query)
            search_collection.insert_one({"user_query": user_query, "search_results": search_results})
            st.write(search_results)
            st.success("Search results have been saved.")
        except Exception as e:
            st.error(f"An error occurred during search: {e}")

    if st.button("Summarized Search"):
        db_search = search_collection.find_one({"user_query": user_query})
        if not db_search:
            st.warning("Please perform the actual search first.")
        else:
            try:
                summary = summarization_chain.run({"input": user_query, "context": db_search['search_results']})
                st.write(summary)
                summary_dict = {user_query: summary}
                summary_collection.insert_one(summary_dict)
                st.success("Summarized search results have been saved.")
            except Exception as e:
                st.error(f"An error occurred during summarization: {e}")
