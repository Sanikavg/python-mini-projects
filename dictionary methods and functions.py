month={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
print("Dictionary: ",month)
print('''**************DICTIONARY METHODS AND FUCNTIONS*********************
1. find the length of dictionary(key-value pairs)
2. get a value from the dictionary
3. return list of keys in dictionary
4. return list of values in dictionary
5. clear all items from the dictionary
6. delete single item in dictionary
7. delete last element only
8. return key-value pairs as tuples in a list
9. add a dictionary or element
10. copy dictionary
11. sort elements in ascending/descending order
12. find minimum and maximum key in dictionary
13. EXIT''')
while True:
   choice=int(input("Enter choice: "))
   if choice==1:
      print(len(month))
   if choice==2:
      key=input("Enter key to be searched: ")
      print(month.get(key,'Not Available'))
   if choice==3:
      print(month.keys())
   if choice==4:
      print(month.values())
   if choice==5:
      month.clear()
      print("Dictionary is empty")
   if choice==6:
      item=input("enter key to be deleted: ")
      if item in month:
         print("Deleting",item,"...")
         del(month[item])
      else:
         print(item,"not available in dictionary")
   if choice==7:
      print(month.popitem(),"is deleted from dictionary")
   if choice==8:
      print(month.items())
   if choice==9:
      add=eval(input("Enter element/dictionary to be added: "))
      month.update(add)
      print("new dictionary: ",month)
   if choice==10:
      print(month.copy())
   if choice==11:
      order=input("Enter ascending or descending order (a/d): ")
      if order=='a':
         print(sorted(month))
      elif order=='d':
         print(sorted(month,reverse=True))
   if choice==12:
      print("minimum key:value is ",min(month),min(month.values()))
      print("minimum key:value is ",max(month),max(month.values()))
   if choice==13:
      print("quiting program...")
      break
      







      
