balance = 1000
transactions = [("deposit", 500), ("withdraw", 300),
                ("withdraw", 1500), ("deposit", 200)]

for kind, amount in transactions:
    if amount <= 0:
        print("Invalid amount:", amount)
    elif kind == "deposit":
        balance += amount
        print("Deposited:", amount)
    elif kind == "withdraw":
        if amount <= balance:
            balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Rejected withdrawal:", amount, "- insufficient balance")

print("Final balance:", balance)
