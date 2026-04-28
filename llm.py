import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

SCHEMA = """
transactions(id, user_id, amount, category, merchant, transaction_date)
"""

def generate_sql(question, user_id):
    prompt = f"""
Convert this question into SQL.

Schema:
{SCHEMA}

Rules:
- Filter user_id = {user_id}
- Use SQLite syntax
- Return only SQL

Question:
{question}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response['choices'][0]['message']['content']


def generate_insight(result, question):
    prompt = f"""
Explain this result in simple words.

Question: {question}
Result: {result}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response['choices'][0]['message']['content']