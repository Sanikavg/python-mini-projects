s=input("Enter string: ")
s1=""
space=" "
for i in s:
    if i.isalnum():
        s1=s1+i
        s1+=space
print(s1)

        
