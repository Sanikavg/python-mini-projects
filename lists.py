l=['hi',7,'bye',8,79,'world',34,56]
l2=[yes,no,5,6]
l3=l+l2#can also be written as:
for i in l2:
    l.append(i)
l2=l.copy#copy function also be wriiten as:
l2=list(l)#list function
print(l)
print(l[2:])#slicing of list
print(l[1:6])
print(l[:4])
print(l[-4:-1])#print value of -4,-3,-2
l.remove("hi")#to remove a specific element
l.pop()#to remove last elemnt
l.append("orange")#add element in last position
l.insert(2,"kiwi")#add element in a specific position
l[1]=20#replace/change an item in list
for i in l:
    print (i)
if "hi" in l:
    print("yes")
else:
    print("no")

del l#remove list
l.clear()#output will be []
