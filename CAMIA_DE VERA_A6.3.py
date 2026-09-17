import re
id = input("Enter your ID: ")
pattern = r"\d{4}-\d{4}"
if re.fullmatch(pattern, id):
    print("Valid Student ID.")
else:
    print("Invalid Student ID.")