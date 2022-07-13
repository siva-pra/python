###class and object

'''class human():
    color= "block"
    height= 2.5
    def run(self):
        print("running.....")
    def walk(self):
        print("walking...")
siva=human()
print(siva.color)
print(siva.height)
siva.run()
siva.walk()
'''

'''class human():  #class
    def __init__(self,cd,hf): # inhertance
        self.hight=hf
        self.color=cd
siva=human("block",22)  #object
print(siva.color)
print(siva.hight)
prasad=human("whith",2.5)
print(prasad.color)
print(prasad.hight)'''

### inhertance

#without inheritance:

"""class BaseClass(): #parent class
    a=10
    b=20
    def display(self):
        print("BASE CLASS")
class DerivedClass():  #child class
    c=30
    d=40
    def display(self):
        print("DERIVED CLASS")
bobj=BaseClass()
print(bobj.a)
print(bobj.b)
bobj.display()

dobj=DerivedClass()
print(dobj.c)
print(dobj.d)
dobj.display()"""

#with inheritance:

"""class BaseClass():
    p=10
    q=20
    def display(self):
        print("BASE CLASS")
class DerivedClass(BaseClass):
    m=30
    n=40
    def run(self):
        print("DERIVED CLASS")
bobj=BaseClass()
print(bobj.p)
print(bobj.q)
bobj.display()

dobj=DerivedClass()
print(dobj.m)
print(dobj.n)
dobj.run()

print(dobj.p)
print(dobj.q)
dobj.display()"""

##single ingheritance   = child class (derived class) access the parent class (base class) => consists of one child and parent
"""
class BaseClass(): #parent class
    p=10
    q=20
    def display(self):
        print("BASE CLASS")
class DerivedClass(BaseClass): #child class
    m=30
    n=40
    def run(self):
        print("DERIVED CLASS")
dobj=DerivedClass()
print(dobj.m)
print(dobj.n)
dobj.run()

print(dobj.p)
print(dobj.q)
dobj.display()"""

##multilevel inheritance  child class access the both parent and grand prent
"""
class GrandClass():  #grand parent 
    a=10 
    b=20
    def displays(self):
        print("GRAND CLASS")

class BaseClass(GrandClass):  #parent =>access the  grand parent
    p=10
    q=20
    def display(self):
        print("BASE CLASS")
class DerivedClass(BaseClass): #child => acces the parent and grand parent
    m=30
    n=40
    def run(self):
        print("DERIVED CLASS")

gobj=GrandClass()
print(gobj.a)
print(gobj.b)
gobj.displays()


bobj=BaseClass()
print(bobj.a)
print(bobj.b)
bobj.displays()

print(bobj.p)
print(bobj.q)
bobj.display()


dobj=DerivedClass()
print(dobj.m)
print(dobj.n)
dobj.run()

print(dobj.p)
print(dobj.q)
dobj.display()

print(dobj.a)
print(dobj.b)
dobj.displays()"""

## herithical inheratance  = one base class and two child class
"""
class BaseClass(): #parent class
    p=10
    q=20
    def displays(self):
        print("BASE CLASS")
class DerivedClassson(BaseClass): #child class1
    m=30
    n=40
    def runs(self):
        print("DERIVED CLASS1")
class DerivedClasssons(BaseClass): #child class2
    a=50
    b=60
    def run(self):
        print("DERIVED CLASS2")
bobj=BaseClass()
print(bobj.p)
print(bobj.q)
bobj.displays()

son=DerivedClassson()
print(son.p)
print(son.q)
son.displays()
print(son.m)
print(son.n)
son.runs()

sons=DerivedClasssons()
print(sons.p)
print(sons.q)
sons.displays()
print(sons.a)
print(sons.b)
sons.run()"""

## multiple inheritance
"""
class Father(): #parent class
    p=10
    q=20
    def displays(self):
        print("father")
class Mother(): #mother class
    m=30
    n=40
    def runs(self):
        print("mother")
class DerivedClass(Father,Mother): #child class
    a=50
    b=60
    def run(self):
        print("DERIVED CLASS")

sons=DerivedClass()
print(sons.p)
print(sons.q)
sons.displays()
print(sons.m)
print(sons.n)
sons.runs()
print(sons.a)
print(sons.b)
sons.run()
"""
###polymaphisum:
##runtime polymaphisum  => accesing method overwriting
"""
class Parent():
    def transfort(self):
        print("cycle")
class Child(Parent):
    def transfort(self):
        print("bike")
ch=Child()
ch.transfort()
"""

## encapulation and datahiding
#public access
"""class Public():
    a=10
    b=100
    def display(self):
        print("public")
obj=Public()
print(obj.a)
print(obj.b)
obj.display()
"""
#private access

"""class Private():
    __a=1
    b=2
    def display(self):
        print("private")
        print(self.__a)
obj=Private()
print(obj.b)
obj.display()"""
#print hide date
"""class Private():
    __a=1
    b=2
    def __display(self):
        print("private")
        print(self.__a)
    def show(self):
        self.__display()
obj=Private()
print(obj.b)
obj.show()"""
#hide date
"""class Private():
    __a=1
    b=2
    def __display(self):
        print("private")
        print(self.__a)
    def show(self):
        self.__display()
obj=Private()
print(obj.b)"""

###MODULES
##buit-in module
#os module

"""import os

print(os.getcwd())
print(os.listdir())
print(os.path)
"""
