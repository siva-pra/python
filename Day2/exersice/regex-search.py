import re

name = "Hello Tellagorla Siva Prasad"
search = r"a"
find= re.search(search,name)
if find:
    print( "search found:", find.group()) 
else:
    print("No search found.")
