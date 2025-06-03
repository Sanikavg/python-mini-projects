l=eval(input("Enter list: "))
newL=[]
for i in l:
    if len(i)%2==0:
        print(i)
    else:
        newL.append(i)
print("New List= ",newL)
