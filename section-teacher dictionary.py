classxi={}
n=int(input("Enter total number of sections: "))
for i in range(n):
    section=input("Enter section: ")
    teacher=input("Enter class teacher's name: ")
    classxi[section]=teacher
print("Class",'\t',"teacher's name")
for i in classxi:
    print("XI",'\t',i,'\t',classxi[i])
