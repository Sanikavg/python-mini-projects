
def details(student, n):
    for i in range(n):
        print("Student",i+1)
        rollno = int(input("Enter rollno: "))
        name = input("Enter name: ")
        marks = int(input("Enter mark: "))
        student[rollno] = [name,marks]
        print()

def display(student):
    global count_s
    count_s = 0
    print("Students with marks above 75: ")
    for i in student:
        if student[i][1] > 75:
            print(student[i][0])
            count_s += 1

student = {}
n = int(input("Enter number of students: "))
print()
details(student, n)

display(student)

if count_s == 0:
    print("None of the students have scored above 75")
    
