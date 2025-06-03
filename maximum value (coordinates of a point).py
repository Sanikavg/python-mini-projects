my_points={'a':(4,3),'b':(1,2),'c':(5,1)}
maxi=0

for i in my_points.values():
    if i[0]>maxi:
        maxi=i[0]
print("At index 0: ",maxi)

maxi=0
for i in my_points.values():
    if i[1]>maxi:
        maxi=i[1]
print("At index 1: ",maxi)  
