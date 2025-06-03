str=input("enter a string: ")
b=str.capitalize()#only first letter of entire string gets capitalized
b=str.title()#it makes the first letter of each word capital
print(b)
a="Let it be, let it be, let it be"
c=a.find("let it")#it gives position of first occurrence of the string and is case sensitive
print(c)
for i in range (0,len(str),+2):
    print(str[i],str[i+1])
