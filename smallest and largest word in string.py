s=input("enter string: ")
l = list(s.split())

      
small = large = l[0]
   
 
for k in range(0, len(l)):
    if(len(small) > len(l[k])):
        small = l[k]
    if(len(large) < len(l[k])):
        large = l[k]
print(small,large)
