scores = {
    "Amina": {"python": 82, "statistics": 76, "calculus": 88},
    "Maya": {"python": 58, "statistics": 64, "calculus": 61},
    "Disha": {"python": 91, "statistics": 89, "calculus": 94},
    "Nora": {"python": 45, "statistics": 52, "calculus": 56}
}

results = {}

for student in scores:
    marks = scores[student]

    average = round(sum(marks.values()) / 3, 2)

    if average >= 60:
        status = "Pass"
    else:
        status = "Fail"

    results[student] = {"average": average, "status": status}

print(results)
