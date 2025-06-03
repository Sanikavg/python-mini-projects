d={}
n=int(input("Enter number of friends: "))
for i in range(n):
    name=input("enter name: ")
    phone=int(input("enter phone number: "))
    d[name]=phone
print("Phonebook")
print(d)
delete=input("enter name to be deleted: ")
print(d.pop(delete,'not available'))
print("new phonebook: ",d)
