import re

url = input("Enter your twitter profile URL: ").strip()

matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))