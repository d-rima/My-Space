from quiz_data import question_data

questions = []

problem_no = 0

score = 0

class question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


for i in range(len(question_data)):
    questions.append(question(question_data[i]["text"], question_data[i]["answer"]))

for problem in questions:
    user_answer = input((f"{problem.text} Type 'True' or 'False': "))
    problem_no += 1
    if user_answer == problem.answer:
        print("That is correct.")
        score += 1
        print(f"You have answered {score}/{problem_no} correctly.")
    else:
        print("That is incorrect.")
        print(f"You have answered {score}/{problem_no} correctly.")

