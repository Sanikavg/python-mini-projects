
def gb(s,a,r):
    global n
    if s==n:
        return (a*(r**(s-1)))
    else:
        print(a*(r**(s-1)))
        return gb(s+1,a,r)
s=1
n=int(input())
a=int(input())
r=int(input())
print(gb(s,a,r))
    
    
