l1=eval(input("Enter list: "))
val=int(input("search: "))
for i in range(len(l1)):
    if l1[i]==val:
        print(" found at index number",i)
