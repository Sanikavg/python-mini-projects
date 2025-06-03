print("PATTERN 1")
print()
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
print()
print("PATTERN 2")
print()
for i in range (1,6):
    num=ord('A')
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end="")
        num+=1
    print()
print()
print("PATTERN 3")
