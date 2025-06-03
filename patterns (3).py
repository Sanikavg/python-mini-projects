print("PATTERN 1")
print()
for i in range(1,6):
    for j in range(0,i):
        print(i,end="")
    print()
print()
print("PATTERN 2")
print()
for i in range (1,5+1):
    num=ord('A')
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end="")
        num+=1
    print()
print()
print("PATTERN 3")
print()
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
