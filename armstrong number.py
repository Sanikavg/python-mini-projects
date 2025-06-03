#print 1 to 1000 armstrong number
num=1
print("The arm strong numbers from 1 to 999 are: ")
while(num<=999):
        sum=0
        temp=a=num
        power=len(str(num))
        while (a>0):
            value=a%10
            sum=sum+value**power
            a=a//10

        if sum==temp:
            print(temp)
        num=num+1
