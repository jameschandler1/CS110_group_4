# Gilbert Collado

question = "What is the capital of France?"
choices = {
    "A": "Berlin",
    "B": "Madrid",
    "C": "Paris",
    "D": "Rome"
}
correct_answer = "C"

# Display question
print(question)
for key, value in choices.items():
    print(f"{key}. {value}")

# Get user input
answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

# Check correctness
if answer == correct_answer:
    print("\nCorrect! 🎉")
else:
    print("\nIncorrect.")
    print(f"The correct answer is {correct_answer}: {choices[correct_answer]}")
