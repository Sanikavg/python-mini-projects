l1=eval(input("Enter list: "))
l2=eval(input("Enter list: "))

for i in l1:
    for j in l2:
        if i==j:
            print("Overlapped")
            break
    break
else:
    print("Seperated")
        
    
