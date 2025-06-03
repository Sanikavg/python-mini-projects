'''def list_function():
    l=eval(input("enter list: "))
    for i in l:
        if i%2==0:
            print(i)
list_function()'''


a=input()
list=a.split()
print(list)
sum=0
for i in list:
    sum+=int(i)
print(sum)
