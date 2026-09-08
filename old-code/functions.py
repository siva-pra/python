###### funtions
## fuction call
def display():
    print("hello siva")
display()

def display(stg):
    print("hello", stg)
display("prasad")

def display(a,b):
    c=a*b
    print(c)
display(10,5)

##types of argments
#required argment
def display(a,b):
    print(a,b)
display(10,20)

#default argments
def display(b,a):
    print(a,b)
display(1,2)
#keyword argmernts
def display(b,a=10):
    print(a,b)
display(1)

#arbitory argments
def display(*maxs):
    print(maxs)
display(10,20,30)

def display(*maxs):
    print(maxs[1])
display(10,20,30)

##multi return
def display(a,b):
    c=a+b
    return c
res=display(10,20)
print(res)

##local and globel
a=10
def display():
    print(a)
display()

a=10
def display():
    a=100
    print(a)
display()
print(a)

#globel
a=10
def display():
    global a
    a=a+1
    print(a)
display()

## lambda funtion

a=lambda a,b:a+b
print(a(10,11))

a=lambda a,b:a*b
print(a(10,11))

a=lambda a:a*a
print(a(10))

## recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))
