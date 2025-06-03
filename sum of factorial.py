sum=0
f=1
j=1
n=int(input("Enter the value of n:"))
if n>0:
 for i in range(1,n+1):
     while j<=i:
        f=f*i
        j+=1
     sum+=f
 print("the factorial of",n,"is",sum)
else:
    print("FACTORIAL NOT DEFINED FOR NEGATIVE VALUES")
