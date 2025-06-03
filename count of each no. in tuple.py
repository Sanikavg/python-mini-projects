t=(1,2,3,1,3,3,5,2,2,1)
l=[]
for i in range(0,len(t)):
    count=1
    
    if t[i] not in l:
      for j in range(i+1,len(t)):
        
          if t[i]==t[j]:
            count+=1
            
      print("the count of element",t[i],"is: ",count)
      if count>1:
         l.append(t[i])

