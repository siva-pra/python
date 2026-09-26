# list of index : to print the single value in alist index start from 0 
list = [1,3,7,2,5, 8,6,4,10,9]
# print the 3 value
list_index =list[1]
print("index =",list_index)

# length of list
length_list = len(list) 
print("length of list =",length_list)

# add the values in list
add = list.append("siva")
print("append list =",list)

# remove the value in list
rm = list.remove("siva")
print("remove list =", list)

# sort asseding order
order = list.sort()
print("ordering list =", list)

# slicing : print range of vlaues in list
slc = list[0:5]
print("slicing list =",slc)

# concatination: add the two or more values in list
con = list + ["siva","prasad"]
print("concatination list =",con)

# checking the elemants
elemant = 'prasad' in con
print (elemant)
