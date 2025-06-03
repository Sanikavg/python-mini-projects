from random import randrange

def counter(start,stop):
    count_even=count_odd=0
    for i in range(100):
        num=randrange(start,stop)
        print(num)
        if num%2==0:
            count_even+=1
        else:
            count_odd+=1
        
    print("count of even numbers: ",count_even)
    print("count of odd numbers: ",count_odd)

start=int(input("Enter the start range value: "))
stop=int(input("Enter the stop range value: "))
counter(start,stop)

    
    
