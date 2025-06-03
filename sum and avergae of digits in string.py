s=input("enter string: ")
mark=[]

for i in s.split():
    
    if i.isdigit()==True:
        i=int(i)
        
        mark.append(i)

print("sum is =",sum(mark),"and average= ",sum(mark)/len(mark))       
