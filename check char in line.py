l=input("Enter a line: ")
count={'characters':0,'words':0,'vowels':0,'consonants':0,'digits':0}
for i in l:
    if i.isdigit():
        count['digits']+=1
    elif i.isalpha():
        if i in 'aeiouAEIOU':
            count['vowels']+=1
        else:
            count['consonants']+=1
    
    if i!=' ':
        count['characters']+=1
for i in l.split():
    if i.isalpha():
        count['words']+=1
print(count)
    
