str=input("Enter a string: ")
ch=input("Enter a character: ")
count=0
for i in str:
    if i==ch:
        count+=1
print(ch,"is present",count,"times in",str)
