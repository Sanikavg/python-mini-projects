def vowelcount(s):
    count_v=0
    for i in s:
        if i in 'aeiouAEIOU':
            count_v+=1
    return count_v

def consonantcount(s):
    count_s=0
    for i in s:
        if i not in 'aeiouAEIOU' and i.isalpha()==True:
            count_s+=1
    return count_s

def uppercount(s):
    count_u=0
    for i in s:
        if i>='A' and i<='Z':
            count_u+=1
    return count_u

def lowercount(s):
    count_l=0
    for i in s:
        if i>='a' and i<='z':
            count_l+=1
    return count_l


print("\t\t MENU")
print('''1) count number of vowels.
2) count number of consonants.
3) count number of uppercase letters.
4) count number of lowercase letters.
5) EXIT''')
print()
while True:
    c=int(input("Enter choice: "))
    if c==1:
        s=input("Enter string: ")
        print("count of vowels: ",vowelcount(s))
        print()
    if c==2:
        s=input("Enter string: ")
        print("count of consonants: ",consonantcount(s))
        print()
    if c==3:
        s=input("Enter string: ")
        print("count of uppercase letters: ",uppercount(s))
        print()
    if c==4:
        s=input("Enter string: ")
        print("count of lowercase letters: ",lowercount(s))
        print()
    if c==5:
        print("Exit program...")
        break
    
