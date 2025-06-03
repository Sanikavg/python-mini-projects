ch=input("enter a character: ")


for j in range(0,len(ch)):
    i=ch[j]
    if i>='a' and i<='z':
        
        print("The character",ch,"is an alphabet (small letter)")
       
    elif i>='A' and i<='Z':
        
        print("The character",ch,"is an alphabet (capital letter)")

    elif i>='0' and i<='9':#(i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9'):
        
        print("The character",ch,"is a digit")

    else:
        
        print("The character",ch,"is a symbol")
