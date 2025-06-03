n=int(input("Enter number of employees: "))
empinfo={}
i=1
while i<=n:
    num=int(input("Enter employee number: "))
    name=input("Enter name: ")
    empinfo[num]=name
    i+=1
l=list(empinfo.keys())
l.sort()
print("Employee information")
print("Employee Number ","\t","Employee Name")
for i in l:
    print(i,'\t \t \t', empinfo[i])
