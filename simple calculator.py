a=float(input("Enter operand 1: "))
b=float(input("Enter operand 2: "))
op=input("enter the operator: ")
if op=='+':
    sum=a+b
    print(a,"+",b,"=",sum)
elif op=='-':
    diff=a-b
    print(a,"-",b,"=",diff)
elif op=='*':
    pro=a*b
    print(a,"*",b,"=",pro)
elif op=='/':
    quo=a/b
    print(a,"/",b,"=",quo)
elif op=='%':
    rem=a%b
    print(a,"%","=",b,rem)
