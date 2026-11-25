marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]

valid_marks = []

for mark in marks:
    if mark >= 0 and mark <= 100:
        valid_marks.append(mark)

grades = {"A": 0, "B": 0, "C": 0, "F": 0}

for mark in valid_marks:
    if mark >= 80:
        grades["A"] = grades["A"] + 1
    elif mark >= 70:
        grades["B"] = grades["B"] + 1
    elif mark >= 60:
        grades["C"] = grades["C"] + 1
    else:
        grades["F"] = grades["F"] + 1

total = 0

for mark in valid_marks:
    total = total + mark

average = total / len(valid_marks)

print("Valid marks:", valid_marks)
print("Grade counts:", grades)
print("Average: {:.2f}".format(average))