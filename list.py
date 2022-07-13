### list

'''lis=[10,20,30,40]
print(type(lis))
print(lis)'''
### accesing

'''print(lis[0])
print(lis[-1])'''

###slicing
'''for i in range(10):
    print(i, end=" ")
for a in range(2,10,1):
    print(a, end=" ")'''

### reassing list element
'''print(lis)
lis[2]=35
print(lis)'''

##### multidementional list

'''ss=[[10,20,40],[22,450,60]]
print(ss[1])
print(ss[1][1])'''

## basic operator
'''# add
a=[10,20,30]
b=[40,50,60,70]
c=(a+b)
print(c)

## *
print(a*2)
print(b*2)

## len
print(len(a),len(b))

## min and max
print(min(a),max(b))

### sum
print(sum(a+b))

## membership
print(10 in a)
print(70 in a)

## ituration using for loop

for i in range(10):
     print(i, end=",")'''

### built in operation
'''ls=[]
print(ls)
##append
ls.append(10)
print(ls)
##extand
ls.extend([120,30])
print(ls)
##insert
ls.insert(1,22)
print(ls)
## sort => asending order
ls.sort()
print(ls)
## count
print(ls.count(10))
##index
c=ls.index(30)
print(c)
##pop
d=ls.pop()
print(d)
print(ls)
##reverse
e=ls.reverse()
print(ls)
##remove
ls.remove(10)
print(ls)
##delete
del.ls()
print(ls)'''

###list comprehension

a=[ele*ele for i in ele(10)]