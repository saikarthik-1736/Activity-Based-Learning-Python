subjects = ["Python", "Maths", "English"]
test1 = [65, 72, 80]
test2 = [78, 68, 85]
for i in range(len(subjects)):
 change = test2[i] - test1[i]
 if change > 0:
  result = "improved by " + str(change)
 elif change < 0:
   result = "declined by " + str(-change)
 else:
  result = "no change"
 print(subjects[i] + ":", result)