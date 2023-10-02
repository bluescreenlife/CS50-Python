import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|org|net|edu|gov)$", email):
    print("Valid")
else: 
    print("Invalid")