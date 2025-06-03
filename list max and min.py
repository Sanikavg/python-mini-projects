L1=eval(input("Enter list: "))
maximum=minimum=0

for i in L1:
    if i>maximum:
        maximum=i
    else:
      for j in L1:
             if j<i or j<minimum:
                minimum=j
            
print("Maximum is",maximum)
print("Minimum is ",minimum)
