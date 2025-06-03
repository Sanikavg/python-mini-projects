def grade(mark):
    if mark in range(91,101):
        print("A1 \t\t 10.0")
    elif mark in range(81,91):
        print("A2 \t\t 9.0")
    elif mark in range(71,811):
        print("B1 \t\t 8.0")
    elif mark in range(61,71):
        print("B2 \t\t 7.0")
    elif mark in range(51,61):
        print("C1 \t\t 6.0")
    elif mark in range(41,51):
        print("C2 \t\t 5.0")
    elif mark in range(33,41):
        print("D \t\t 4.0")
    elif mark in range(21,33):
        print("E1 \t\t 0.0")
    elif mark in range(0,21):
        print("E2 \t\t 0.0")

def display():
    print("\t\t\t REPORT CARD")
    print("Name:",name)
    print()
    print("Subject \t\t Marks \t\t Grade \t\t Grade Point")
    print("--------------------------------------------------------------")
    for i in report:
        print(i,"\t\t",report[i],"\t\t",end=' ')
        grade(report[i])
        print()


report={}
name=input("Enter name of student: ")
mark1=float(input("Enter your English marks: "))
report['English']=mark1
mark2=float(input("Enter your Math marks: "))
report['Math']=mark2
mark3=float(input("Enter your Physics marks: "))
report['Physics']=mark3
mark4=float(input("Enter your Chemistry marks: "))
report['Chem']=mark4
mark5=float(input("Enter your Computer marks: "))
report['Comp']=mark5
print()
display()
    




