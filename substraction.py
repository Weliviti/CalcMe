import random
import time

#start timer
start_time = time.time()

score = 0

for i in range(1,11):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct_answer = num1 - num2

    print(f"\nQuestion {i}: What is {num1} - {num2}?")

    try:
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {correct_answer}.")
    except ValueError:
        print("⚠ Please enter a valid number.")

# Stop timer
end_time = time.time()
total_time = round(end_time - start_time, 2)

# Results
print("\n=== RESULTS ===")
print(f"Total Correct Answers: {score}/10")
print(f"Total Time Taken: {total_time} seconds")