marks = [
 [80, 75, 90],
 [65, 70, 72],
 [92, 88, 95]
]
for i in range(len(marks)):
 total = sum(marks[i])
 average = total / len(marks[i])
 print("Student", i + 1, "total:", total,
 "average:", round(average, 2))
subject_totals = [0, 0, 0]
for row in marks:
 for j in range(len(row)):
  subject_totals[j] += row[j]
for j in range(len(subject_totals)):
 print("Subject", j + 1, "total:", subject_totals[j])