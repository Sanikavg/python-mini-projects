limit=int(input("How many numbers do you wish to enter? "))
sum=0
for i in range(1,limit+1):
    num=int(input("Enter number: "))
    sum+=num
avg=sum/limit
print("The sum of the numbers is",sum,"and average is",avg)
