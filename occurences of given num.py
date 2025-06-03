t=eval(input("enter tuple: "))
n=int(input("enter number: "))
count=0
for i in t:
    if i==n:
        count+=1
print("Occurrences of number ",n,"in",t,"are",count)
