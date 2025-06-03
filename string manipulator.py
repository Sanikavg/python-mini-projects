def upit(s):
    s2=''
    for i in s:
        if i>='a' and i<='z':
            s2+=chr(ord(i)-32)
        else:
            s2+=i
    return s2

def loit(s):
    s2=''
    for i in s:
        if i>='A' and i<='Z':
            s2+=chr(ord(i)+32)
        else:
            s2+=i
    return s2

def length(s):
    len_s=0
    for i in s:
        len_s+=1
    return len_s

def scopy(s):
    copy=''
    for i in s:
        copy+=i
    return copy

def sconcat(s1,s2):
    s3=''
    for i in s1:
        s3+=i
    for j in s2:
        s3+=j
    return s3

print("\t\t MENU")
print('''1. convert the string to uppercase
2. convert the string into lowercase
3. Calculate the length of the string
4. copy the string
5. concatenate two strings
6. EXIT''')
print()
while True:
    c=int(input("Enter choice: "))
    
    if c==1:
        s=input("Enter string: ")
        print("Uppercase: ",upit(s))
        print()
    if c==2:
        s=input("Enter string: ")
        print("Lowercase: ",loit(s))
        print()
    if c==3:
        s=input("Enter string: ")
        print("Length: ",length(s))
        print()
    if c==4:
        s=input("Enter string: ")
        print("Copy: ",scopy(s))
        print()
    if c==5:
        s1=input("Enter string 1: ")
        s2=input("Enter string 2: ")
        print("New string: ",sconcat(s1,s2))
        print()
    if c==6:
        print("Exit program...")
        break
    
        
        
    



        
    
            
