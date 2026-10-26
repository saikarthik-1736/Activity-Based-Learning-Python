password = input("Enter a password: ")
if len(password) < 8:
 print("Password must contain at least 8 characters.")
elif not any(ch.isupper() for ch in password):
 print("Add at least one uppercase letter.")
elif not any(ch.islower() for ch in password):
 print("Add at least one lowercase letter.")
elif not any(ch.isdigit() for ch in password):
 print("Add at least one digit.")
elif password.isalnum():
 print("Add at least one special character.")
else:
 print("Password meets the basic policy.")