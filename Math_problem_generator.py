import random
import time

MAX_NUMBER = 100
MIN_NUMBER = 2
OPERATIONS = ['+', '-', '*']
NUMBER_OF_PROBLEMS = 10


def generate_math_problem():
    left_operand = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_operand = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)

    problem_expression = f"{left_operand} {operation} {right_operand}"
    answer = eval(problem_expression)

    return problem_expression, answer


wrong_answers_count = 0

start_quiz = input("Enter 'y' to start the math quiz: ")
if start_quiz.lower() != 'y':
    quit()
print("____________________________________")

start_time = time.time()

for i in range(NUMBER_OF_PROBLEMS):
    problem, correct_answer = generate_math_problem()

    while True:
        user_answer = input(f"Problem #{i + 1}: {problem}= ")
        if user_answer == str(correct_answer):
            break

        wrong_answers_count += 1

end_time = time.time()

total_time_taken = round(end_time - start_time, 2)
print("____________________________________")
print(f"You finished the test in {total_time_taken} seconds")
print(f"You got {wrong_answers_count} wrong answer(s)")
