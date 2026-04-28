from fastapi import FastAPI
from models import QueryRequest
from db import (
    execute_query,
    save_query_history,
    get_query_history,
    get_total_spending,
    get_spending_by_category,
    get_top_category
)
from llm import generate_sql, generate_insight
from cache import get_cache, set_cache

app = FastAPI()


@app.post("/query")
def query(data: QueryRequest):

    cache_key = f"{data.user_id}:{data.question}"

    cached = get_cache(cache_key)
    if cached:
        return {"source": "cache", "response": cached}

    try:
        sql = generate_sql(data.question, data.user_id)
        result = execute_query(sql)

        if not result:
            return {"response": "No data found"}

        insight = generate_insight(result, data.question)

        save_query_history(
            data.user_id,
            data.question,
            sql,
            result,
            insight
        )

        set_cache(cache_key, insight)

        return {
            "sql": sql,
            "result": result,
            "insight": insight
        }

    except Exception as e:
        return {"error": str(e)}


@app.get("/history/{user_id}")
def history(user_id: int):
    return {"history": get_query_history(user_id)}


@app.get("/analytics/{user_id}")
def analytics(user_id: int):
    return {
        "total_spending": get_total_spending(user_id),
        "spending_by_category": get_spending_by_category(user_id),
        "top_category": get_top_category(user_id)
    }