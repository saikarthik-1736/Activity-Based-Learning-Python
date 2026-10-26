rows = int(input("Enter number of rows: "))
if rows <= 0:
 print("Please enter a positive number.")
else:
 for i in range(1, rows + 1):
   print(" " * (rows - i) + "* " * i)