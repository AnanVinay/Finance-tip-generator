import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

load_dotenv()

# AI Model Init
chat_model = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Function to Get Finance Tips
def get_finance_tips(income, expenses, savings_goal):
    prompt = (
        f"You are a financial assistant.\n\n"
        f"Based on the user's details:\n"
        f"- Monthly Income: {income}\n"
        f"- Monthly Expenses: {expenses}\n"
        f"- Monthly Savings Goal: {savings_goal}\n\n"
        f"Provide 3 actionable, personalized finance tips to improve budgeting or saving."
    )
    response = chat_model([HumanMessage(content=prompt)])
    return response.content.strip()

# Streamlit UI
st.set_page_config(page_title="AI Finance Tips")

st.title("💡 AI-Powered Personal Finance Tips")

with st.form("finance_form"):
    income = st.number_input("Monthly Income", min_value=0.0, step=100.0)
    expenses = st.number_input("Monthly Expenses", min_value=0.0, step=100.0)
    savings_goal = st.number_input("Monthly Savings Goal", min_value=0.0, step=100.0)

    submitted = st.form_submit_button("Get AI Tips")

if submitted:
    with st.spinner("Generating tips..."):
        ai_tips = get_finance_tips(income, expenses, savings_goal)
        st.success("Here are your personalized tips:")
        st.write(ai_tips)
