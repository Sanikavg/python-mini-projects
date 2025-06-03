dict={}
d2={}

n=int(input("Enter the length of dict: "))
for i in range(n):
    key=str(input("enter key: "))
    value=int(input("enter value: "))
    dict.update({key:value})
print(dict)

for key,value in dict.items():
    if value not in d2.values():
        d2[key]=value
print(d2)   

l=[v for v in d2.values()]
print(l)
