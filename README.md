# Personal Finance Tip Generator

An AI-powered finance advice application that provides simple budgeting and savings suggestions based on your income, expenses, and financial goals. Built with Google Gemini, LangChain, and FAISS, this app offers personalized, context-aware financial tips to help users better manage their money.

🔗 **[Live Demo](https://your-finance-app-url.onrender.com/)** (Note: The application may take up to 50 seconds to load due to hosting constraints on the free tier.)

## Features

- **AI-Generated Financial Advice**: Receive actionable, personalized budgeting and saving suggestions.  
- **Context-Aware Recommendations**: Utilizes a RAG (Retrieval-Augmented Generation) approach with finance examples to improve tip relevance.  
- **Simple Web Interface**: Enter income, expenses, and savings goal to get immediate suggestions.  
- **Responsive UI**: Clean, mobile-friendly interface built with Bootstrap.  
- **Secure API Management**: Keeps API keys protected using environment variables.  
- **Fast & Extensible**: Lightweight, Flask-based backend, easy to deploy and scale.  

## Tech Stack

- **Frontend**: HTML, CSS (Bootstrap)  
- **Backend**: Python, Flask  
- **AI/LLM**: Google Gemini (`gemini-1.5-flash-001`) via LangChain  
- **Embeddings**: `models/embedding-001` via `GoogleGenerativeAIEmbeddings`  
- **Vector Store**: FAISS (for RAG)  
- **Environment Management**: `python-dotenv`  

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/finance-tip-generator.git
cd finance-tip-generator
```

### 2. Create and Activate a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_google_api_key
PORT=5000
```

### 5. (Optional) Add Finance Examples

You can create a `finance_examples.txt` file with budgeting and saving examples to improve AI responses.

Example format for `finance_examples.txt`:

```
[Basic Budget Tip]
  Allocate at least 20% of your monthly income towards savings and investments.

[Savings Motivation Example]
  Building an emergency fund with 3-6 months of expenses provides financial security.

[Expense Reduction Suggestion]
  Track subscription services and cancel those you rarely use to free up extra cash.
```

### 6. Running the App

```bash
python app.py
```

Visit the app at: [http://localhost:5000](http://localhost:5000)

## File Structure

```
├── app.py                    # Main Flask application
├── templates/                # HTML templates (index.html)
├── static/                   # CSS or JS assets
├── finance_examples.txt      # (Optional) RAG example data
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Dependencies

- Flask  
- python-dotenv  
- langchain  
- google-generativeai  
- faiss-cpu  
- numpy  

### Install them all with:

```bash
pip install -r requirements.txt
```

## Troubleshooting

- **API Key Error**: Ensure `GOOGLE_API_KEY` is correct and has access to Gemini.  
- **FAISS Installation Issues**: If errors occur, reinstall `faiss-cpu` or switch to `faiss-gpu` if your system supports it.  
- **Port Conflict**: Modify the `PORT` value in `.env` if `5000` is in use.  

## How It Works

1. Finance examples from `finance_examples.txt` (if provided) are loaded and chunked using `CharacterTextSplitter`.  
2. Chunks are embedded using `GoogleGenerativeAIEmbeddings` and stored in FAISS for fast similarity search.  
3. User submits financial inputs via the form.  
4. Relevant examples + user input are sent to Gemini using a structured prompt.  
5. Gemini generates personalized finance advice displayed to the user.  

## License

This project is licensed under the MIT License. See the LICENSE file for details.
