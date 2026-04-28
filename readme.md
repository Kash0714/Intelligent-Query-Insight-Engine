# 🤖 Intelligent Query Insight Engine (DISVRAI)

An advanced natural language interface for financial transaction analysis. This engine converts plain English questions into optimized SQL queries, executes them against a SQLite database, and provides human-readable insights using OpenAI's GPT-4.

## 🚀 Features

- **Natural Language to SQL**: Ask questions like "How much did I spend on coffee last month?"
- **AI-Powered Insights**: Get clear, conversational explanations of your data.
- **Transaction Tracking**: Comprehensive history of queries and results.
- **Analytics Dashboard**: Built-in endpoints for spending summaries and category analysis.
- **Fast Performance**: Integrated caching for repeated queries.

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite
- **AI**: OpenAI GPT-4o-mini
- **Environment**: Dotenv for secure configuration

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kash0714/Intelligent-Query-Insight-Engine.git
   cd Intelligent-Query-Insight-Engine
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Copy `.env.example` to `.env`
   - Add your `OPENAI_API_KEY` to the `.env` file.

5. **Initialize the Database**:
   ```bash
   python setup_db.py
   ```

## 🚦 Usage

1. **Start the server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Endpoints**:
   - `POST /query`: Send a JSON body `{"user_id": 1, "question": "your question"}`
   - `GET /history/{user_id}`: Retrieve past queries.
   - `GET /analytics/{user_id}`: Get spending insights.

## 🔒 Security

This project uses a `.gitignore` to ensure that sensitive files like `.env` (API Keys) and `.db` (Local Data) are never pushed to the cloud.

---
Created by [Kashik Bhatia](https://github.com/Kash0714)
