d1={}
d2={}
l=[]
a=int(input("Enter total number of values in Dictionary 1: "))
b=int(input("Enter total number of values in Dictionary 2: "))
print("Enter key and value pairs of dictionary 1 ")
for i in range(a):
    k=input("Enter key: ")
    v=input("enter value: ")
    d1[k]=v
print("Enter key  and value pairs of Dictionary 2 ")
for j in range(b):
    k=input("Enter key: ")
    v=input("Enter value: ")
    d2[k]=v

m=0
for e in d1:
    if e in d2:
        l+=e
        m+=1
if m>0:
    print("overlapped keys are: ",l)
else:
    print("Overlapped keys are None")
