import random
import time

#start timer
start_time = time.time()

score = 0

for i in range(1,11):
    divisor = random.randint(2, 12)
    quotient = random.randint(2, 10)
    dividend = divisor * quotient  # ensures exact division

    correct_answer = quotient
    print(f"Question {i}: What is {dividend} ÷ {divisor}?")

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