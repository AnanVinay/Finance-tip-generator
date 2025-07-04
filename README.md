# AI Finance Tips Generator

An AI-powered finance advice application that provides personalized budgeting and saving tips based on your income, expenses, and savings goals. Built with Google Gemini and LangChain, this app delivers actionable, context-aware financial advice through a simple Streamlit interface.

🔗 **[Live Demo](#)**
*(Add your live demo link here; note that the application may take a moment to start due to hosting constraints.)*

## Features

- **Personalized Finance Tips**: Get 3 tailored, actionable budgeting and saving suggestions.
- **Context-Aware Recommendations**: Uses LangChain with Google Gemini for relevant advice.
- **Clean & Interactive UI**: Enter your monthly income, expenses, and savings goal easily.
- **Fast & Lightweight**: Streamlit-based for rapid responsiveness and easy deployment.
- **Secure API Key Handling**: Environment variables keep your API keys safe.

## Tech Stack

- **Frontend & Backend**: Python, Streamlit
- **AI/LLM**: Google Gemini (`gemini-1.5-flash`) via LangChain
- **Environment Management**: `python-dotenv`

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-finance-tips-manager.git
cd ai-finance-tips-manager
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

Create a `.env` file in the project root with:

```bash
GOOGLE_API_KEY=your_google_api_key
```

Replace `your_google_api_key` with your actual Google Cloud API key that has access to Gemini.

### 5. Running the App

```bash
streamlit run app.py
```

Open your browser and visit [http://localhost:8501](http://localhost:8501)

---

## Sample Finance Tips Format

The app outputs tips like:

```
[Basic Budget Tip]
Allocate at least 20% of your monthly income towards savings and investments.

[Savings Motivation]
Building an emergency fund with 3-6 months of expenses provides financial security.

[Expense Reduction Suggestion]
Track subscription services and cancel those you rarely use to free up extra cash.
```

---

## File Structure

```
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (ignored by git)
├── .gitignore              # Git ignore rules
├── example.txt             # Sample finance tips (optional)
└── README.md               # Project documentation
```

---

## Troubleshooting

- **API Key Issues**: Verify that your `GOOGLE_API_KEY` is valid and has access to Gemini.
- **Dependency Issues**: Run `pip install -r requirements.txt` to install required packages.
- **Port Conflicts**: Streamlit runs on port 8501 by default; change it with `--server.port` if needed.

---

## How It Works

1. User inputs monthly income, expenses, and savings goal.
2. The app builds a prompt incorporating this data.
3. Prompt is sent to Google Gemini via LangChain’s `ChatGoogleGenerativeAI`.
4. Gemini returns personalized finance tips.
5. Tips are displayed in the Streamlit UI.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
