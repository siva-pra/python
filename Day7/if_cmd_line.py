import sys

value = sys.argv[1]

if value == "t2.micro":
    print("this is t2.micro")
elif value == "t3.medium":
    print ("this is t3.medium")
elif value == "t4.xlarge":
    print("this is t4.xlarge")
else:
    print("give correct value")
