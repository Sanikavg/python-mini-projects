def sum2(n):
    global sum1
    sum1+=n%10
    n=int(n/10)
    if n!=0:
        sum2(n)
    return sum1
        

sum1=0
n=int(input())
print(sum2(n))
