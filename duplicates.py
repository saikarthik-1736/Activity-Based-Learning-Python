ids = input("Enter transaction IDs separated by spaces: ").split()
duplicates = []
for item in ids:
 if ids.count(item) > 1 and item not in duplicates:
  duplicates.append(item)
if duplicates:
 print("Duplicate transaction IDs:", duplicates)
else:
 print("No duplicate transactions found.")