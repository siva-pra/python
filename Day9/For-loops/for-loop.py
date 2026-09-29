## for loop is used for range of values(now the value of sequance)
## for loop systex : for    varible    in         sequance
##                  keyword           keyward     range, list, tupple

# basic for loop

for i in range(10):
    print(i)
    
# use list of loops
list = ["tellogorla", 1, "siva", 2, "Prasad", 3]
for name in list:
    print(name)


# incluse the break conditons

list = ["tellogorla", 1, "siva", 2, "Prasad", 3]
for name in list:
    if name == "siva":
        break
    print(name)

for i in range(10):
    if i == 7:
        break
    print(i)

# incluse the continue conditons

list = ["tellogorla", 1, "siva", 2, "Prasad", 3]
for name in list:
    if name == "siva":
        continue
    print(name)

for i in range(10):
    if i == 6:
        continue
    print(i)


s3_buckets = ["siva_bucket","test_buceket", "siva_bucket"]
for s3 in s3_buckets:
    if "siva_bucket" == s3:
     print(s3)

for i in  range(10):
   if i%3 == 1:   
    print(i)


