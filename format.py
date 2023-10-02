import re

name = input("What's your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

## rather, use re

matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")