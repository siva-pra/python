import sys

def addition(a,b):
    add=a+b
    return add
def subtraction(a,b):
    sub=a-b
    return sub
def multipication(a,b):
    mul=a*b
    return mul
def division(a,b):
    div=a/b
    return div
def square(a):
    sq= a**2
    return sq
def persontage(a,b):
    per=a%b
    return per
def cube(a):
    cu=a**3
    return cu

a = float(sys.argv[1])  # cmd line arg a
calucation = sys.argv[2] # cmd line operation add, sub like
b = float(sys.argv[3])   # cmd line arg b

if calucation == "add":
    add = addition(a,b)  ## calling the fuction
    print("addition =",add)

if calucation == "sub":
    sub = subtraction(a,b)
    print("subtraction =",sub)

if calucation == "mul":
    mul = multipication(a,b)
    print("multipication =", mul)

if calucation == "div":
    div = division(a,b)
    print("division =", div)

if calucation == "per":
    per = persontage(a,b)
    print("persontage =", per)

if calucation == "sq":
    sq = square(a)
    print("squre =", sq)

if calucation == "cu":
    cu = cube(a)
    print("cube =", cu)