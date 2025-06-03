l=eval(input("Enter list: "))
num=int(input("Enter number to be searched: "))
count=0
for i in l:
    if i==num:
        print("Number Found")
        break
else:
    print("Number not found")
