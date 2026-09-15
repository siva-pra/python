import re
name = "Siva Prasad"
match = r"Siva"
find= re.match(match,name)
if find:
    print("match-found:",find.group())
else:
    print("No match found.")

