attendance = float(input("Enter attendance percentage: "))
labs = input("Are all labs completed? (yes/no): ").lower()
internal = float(input("Enter internal marks out of 40: "))
fees = input("Are fees cleared? (yes/no): ").lower()
eligible = True
if attendance < 75:
 print("Not eligible: attendance is below 75%.")
 eligible = False
if labs != "yes":
 print("Not eligible: laboratory work is incomplete.")
 eligible = False
if internal < 16:
 print("Not eligible: internal marks are below 16.")
 eligible = False
if fees != "yes":
 print("Not eligible: fees are not cleared.")
 eligible = False
if eligible:
 print("Eligible for the final examination.")