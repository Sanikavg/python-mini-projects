print('''*********MENU*********
1. ADD STUDENT
2. MOD STUDENT
3. DEL STUDENT
4. DISPLAY
5.EXIT''')
students={}
while True:
   choice=int(input("enter choice: "))
   
   if choice==1:
      admin=int(input("Enter admission number: "))
      details=eval(input("enter details: "))
      students[admin]=details
   if choice==2:
      admin=int(input("Enter admission number: "))
      print("Details: ",students.get(admin,'invalid admission number'))
      if admin in students:
         newmarks=eval(input("Enter new marks: "))
         students[admin][3]=newmarks
   if choice==3:
      admin=int(input("enter admin: "))
      if admin in students:
         del(students[admin])
         print("Deleting...")
         print("Successfully deleted")
      else:
         print("invalid admission number")
   if choice==4:
      grade=int(input("Enter Grade: "))
      section=input("Enter section: ")
      for i in students:
         if students[i][2]==section and students[i][1]==11:
            total=sum(students[i][3])
            avg=total/5
            print(students[i],'\t','Total=',total,'\t',"Average=",avg)
      else:
         print("No student in ",grade,":",section)
            
   if choice==5:
      print("Quiting program...")
      break
      
      
      

