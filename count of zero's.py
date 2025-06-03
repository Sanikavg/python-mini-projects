
def count_zero(l):
    if len(l)==0:
        return 0
    
    elif l[0]==0:
        return 1+count_zero(l[1:])
    
    else:
        return 0+count_zero(l[1:])

l=eval(input("Enter array of integers: "))
print(count_zero(l))
