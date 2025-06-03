import csv

def add():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    with open("contacts.csv",'a',newline = '\n') as f:
        wobj = csv.writer(f)
        wobj.writerow([name,phone])

def display():
    with open("contacts.csv",'r') as f:
        robj = csv.reader(f)
        for i in robj:
            print("%s\t%s"%(i[0],i[1]))
def search():
    name = input("Enter name of the person to be searched: ")
    with open("contacts.csv",'r') as f:
        robj = csv.reader(f)
        for i in robj:
            if i[0] == name:
                print("Name: %s\nPhone Number: %s\n"%(i[0],i[1]))
                break
        else:
            print("Name not found")

while True:
    print('''Menu
1. Add contact
2. Display contents of file
3. Search for a given name
4. Exit''')
    ch = int(input("Enter your character: "))
    print()
    if ch == 1:
        add()
        print()
    elif ch==2 :
        display()
        print()
    elif ch==3:
        search()
        print()
    elif ch==4:
        break
    else:
        print("Invalid choice")
        print()
    

    
