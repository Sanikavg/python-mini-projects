s=input("Enter a string: ")
digit=alpha=0
for i in s:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        alpha+=1
print("the number of digits in",s,":",digit)

print("the number of letters in",s,":",alpha)    
    
