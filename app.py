import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.schema import HumanMessage
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

chat_model = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)

def load_finance_examples(file_path="finance_examples.txt"):
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} not found. Starting with empty FAISS index.")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text_splitter.split_text(text)

# Initialize FAISS with finance examples
example_texts = load_finance_examples()

if example_texts:
    db = FAISS.from_texts(example_texts, embedding=embeddings)
else:
    db = FAISS.from_texts(["Initial dummy text to setup FAISS"], embedding=embeddings)

def get_finance_tips_with_rag(income, expenses, savings_goal):
    user_query = f"Income: {income}, Expenses: {expenses}, Savings Goal: {savings_goal}"

    retriever = db.as_retriever(search_kwargs={"k": 3})
    context_docs = retriever.get_relevant_documents(user_query)

    past_context = "\n".join([doc.page_content for doc in context_docs]) if context_docs else "No prior context."

    prompt = (
        f"You are a financial assistant. Use the following context from past interactions if relevant:\n"
        f"{past_context}\n\n"
        f"Based on the user's details:\n"
        f"- Monthly Income: {income}\n"
        f"- Monthly Expenses: {expenses}\n"
        f"- Monthly Savings Goal: {savings_goal}\n\n"
        f"Provide 3 actionable, personalized finance tips to improve budgeting or saving."
    )

    response = chat_model([HumanMessage(content=prompt)])
    ai_tips = response.content.strip()

    combined_text = f"User Details: {user_query}\nAI Tips: {ai_tips}"
    splits = text_splitter.split_text(combined_text)
    db.add_texts(splits)

    return ai_tips

# Streamlit UI
st.title("💡 AI-Powered Personal Finance Tips")

with st.form("finance_form"):
    income = st.number_input("Monthly Income", min_value=0.0, format="%.2f")
    expenses = st.number_input("Monthly Expenses", min_value=0.0, format="%.2f")
    savings_goal = st.number_input("Monthly Savings Goal", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Get AI Tips")

if submitted:
    if income and expenses and savings_goal:
        ai_tips = get_finance_tips_with_rag(income, expenses, savings_goal)
        st.success("Your Personalized Tips:")
        st.info(ai_tips)
    else:
        st.warning("Please fill in all fields.")
