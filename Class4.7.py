scores = [
    [78, 82, 91],
    [65, 70, 68],
    [90, 88, 94],
    [55, 61, 58]
]

averages = []
passing_students = 0

for i in range(len(scores)):
    total = 0

    for j in range(len(scores[i])):
        total += scores[i][j]

    average = total / len(scores[i])
    averages.append(average)

    print("Student", i + 1, "- Total:", total, "Average:", round(average, 2))

    if average >= 60:
        passing_students += 1

highest_average = max(averages)
highest_student = averages.index(highest_average)

print("Averages:", averages)
print("Number of passing students:", passing_students)
print("Index of student with highest average:", highest_student)