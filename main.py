#main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Request model
class Score(BaseModel):
    user_id: int
    total_score: int
    accuracy: float
    time_taken: float
    level: str = "easy"

# Endpoint to save score
@app.post("/save-score/")
def save_score_endpoint(score: Score):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kaito1412",
            database="calcme_db"
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO scores (user_id, total_score, accuracy, time_taken, level)
            VALUES (%s, %s, %s, %s, %s)
        """, (score.user_id, score.total_score, score.accuracy, score.time_taken, score.level))
        conn.commit()
        return {"message": "Score saved successfully", "score_id": cursor.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
