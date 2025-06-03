marks=eval(input("Enter your mark list: "))
sum=0
print("SUM OF MARKS")
for i in marks:
    sum+=i
print(sum)
print("AVERAGE")
print(sum/len(marks))
print("Your maximum marks are ",max(marks))
print("Your minimum marks are ",min(marks))
