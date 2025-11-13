#addition.py
import random
import time
import requests  # To send HTTP request

def run_adding_quiz(user_id, question_count=10, level="easy"):
    score = 0
    start_time = time.time()

    for i in range(1, question_count + 1):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        correct_answer = num1 + num2

        print(f"\nQuestion {i}: What is {num1} + {num2}?")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            print("⚠ Please enter a valid number.")

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    accuracy = round((score / question_count) * 100, 2)

    print("\n=== RESULTS ===")
    print(f"Total Correct Answers: {score}/{question_count}")
    print(f"Total Time Taken: {total_time} seconds")
    print(f"Accuracy: {accuracy}%")

    # Send results to FastAPI
    try:
        response = requests.post("http://127.0.0.1:8000/save-score/",
                                 json={
                                     "user_id": user_id,
                                     "total_score": score,
                                     "accuracy": accuracy,
                                     "time_taken": total_time,
                                     "level": level
                                 })
        if response.status_code == 200:
            print("✅ Results saved to database!")
            print("Response:", response.json())
        else:
            print("❌ Failed to save results:", response.text)
    except Exception as e:
        print("❌ Could not connect to API:", e)

# Example usage
if __name__ == "__main__":
    user_id = 1  # Replace with actual user ID
    run_adding_quiz(user_id)
