def palindrome(s):
    rev=''
    
    for i in range(len(s)-1,-1,-1):
        rev+=s[i]
        
    return rev==s

s=input("Enter string: ")
print("Checking for palindrome...")
print(palindrome(s))


        
        
