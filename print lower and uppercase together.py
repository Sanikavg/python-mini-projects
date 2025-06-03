s=input("Enter: ")
s1=''
s2=''

for i in s:
    if i.islower()==True:
        s1+=i
    elif i.isupper()==True:
        s2+=i
print(s1+s2)
