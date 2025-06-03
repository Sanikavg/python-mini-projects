l=eval(input("Enter list: "))
u=[]
d=[]
for i in l:
    a=l.count(i)
    if a>1 and i not in u:
        u.append(i)
    elif a==1 and i not in d:
        d.append(i)
print("Unique elements are: ",u)
print("Duplicate elements are: ",d)
