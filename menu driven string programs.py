print('''*******Menu*******  
1. Check for Palindrome
2. Extract all digits
3. Change to upper/lower case
4. Replace substrings
5. Exit''')
print()
s=input("Enter string: ")
while True:
    opt=int(input("Enter your choice: "))
    print()
    if opt==1:
        rev=s[::-1]
        if s==rev:
            print(s, "is a palindrome")
        else:
            print(s,"is not a palindrome")
        print()   
    elif opt==2:
        s1=''
        for i in s:
            if i.isdigit():
                s1+=i
        print(s1)
        print()
    elif opt==3:
        print("Uppercase is ",s.upper())
        print("Lowercase is ",s.lower())
        print()
    elif opt==4:
        a=input("Enter substring: ")
        b=input("Enter string to be replaced: ")
        print(s.replace(b,a))
        print()
    elif opt==5:
        print("Exit program....")
        print()
        break
    else:
        print("Enter a valid choice!!!!!!")
        print()
              
        
                
    
    
