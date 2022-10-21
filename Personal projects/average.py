student_scores = input("Input a list of student scores: ").split()
score_average = 0

for i in range(len(student_scores)):
    score_average = score_average + float(student_scores[i])

score_average = score_average/(len(student_scores))

print(score_average)