products = ["Pens", "Books", "Erasers"]
opening = [50, 30, 40]
received = [20, 10, 15]
dispatched = [25, 12, 18]
recorded_closing = [45, 29, 37]
for i in range(len(products)):
 expected = opening[i] + received[i] - dispatched[i]
 difference = recorded_closing[i] - expected
 print(products[i], "expected:", expected,
 "recorded:", recorded_closing[i])
 if difference == 0:
  print(" Stock matches.")
 else:
  print(" Discrepancy:", difference)