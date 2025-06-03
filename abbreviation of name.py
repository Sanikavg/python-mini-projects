name=input("enter full name: ")
s=name.split()
name2=''

for i in range(len(s)):
    if i!=(len(s)-1):
       name2+=s[i][0].upper()+"."
    else:
        name2+=s[i].capitalize()
print(name2)
