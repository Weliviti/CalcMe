import pandas as pd
from dataloader import load_data, save_data
from modeltrainer import train_model
from predictor import predict
from utils import generate_question, ask_question

# Load previous history
df = load_data()
model = train_model(df)

score = 0
question_count = 10

for i in range(1, question_count + 1):
    num1, num2 = generate_question()
    predicted_chance = predict(model, num1, num2)
    
    print(f"\nQuestion {i}")
    print(f"💡 Predicted chance you'll get this right: {round(predicted_chance*100,2)}%")
    
    user_answer, time_taken = ask_question(num1, num2)
    correct_answer = num1 + num2
    correct = int(user_answer == correct_answer)
    score += correct
    
    # Save new data
    new_row = pd.DataFrame([{
        "num1": num1,
        "num2": num2,
        "user_answer": user_answer,
        "correct": correct,
        "time_taken": time_taken
    }])
    df = pd.concat([df,new_row], ignore_index=True)
    save_data(df)
    
    # Retrain model dynamically
    model = train_model(df)

# Results
total_time = round(df.tail(question_count)["time_taken"].sum(),2)
average_time = round(total_time / question_count,2)

print("\n=== RESULTS ===")
print(f"Total Correct Answers: {score}/{question_count}")
print(f"Total Time Taken: {total_time} seconds")
print(f"Average Time per Q.: {average_time} seconds")
