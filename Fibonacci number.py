
def fibonacci():
    a=0
    b=1
    num=int(input("Enter value of n: "))
    for i in range(num):
          n=a+b
          a=b
          b=n
    print(b - a)

fibonacci()
