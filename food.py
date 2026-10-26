prepared = [100, 120, 110, 90, 130]
served = [85, 100, 95, 80, 100]
limit = 15
for i in range(len(prepared)):
 leftover = prepared[i] - served[i]
 waste_percent = (leftover / prepared[i]) * 100
 print("Day", i + 1, "leftover:", leftover,
 "waste:", round(waste_percent, 1), "%")
 if waste_percent > limit:
  print(" Warning: waste is above", limit, "%")
