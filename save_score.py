# save_score.py
import mysql.connector

def save_score(user_id, total_score, accuracy, time_taken, level="easy"):
    """
    Saves the quiz results to the MySQL 'scores' table.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # replace with your MySQL password
            database="calcme_db"
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO scores (user_id, total_score, accuracy, time_taken, level)
            VALUES (%s, %s, %s, %s, %s)
        """, (user_id, total_score, accuracy, time_taken, level))
        conn.commit()
        print("✅ Score saved to database!")
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    finally:
        cursor.close()
        conn.close()
