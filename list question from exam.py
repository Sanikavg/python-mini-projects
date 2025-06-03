l=['Apple','56','orange','67','54','grapes']
a=[]
b=[]
for i in range (0,len(l)):
    if str(l[i]).isdigit():
        a.append(l[i])
        print(l[i],l[i])
    else:
        b.append(l[i])
        print(l[i],"*")
'''for i in b:
    print (i,"*")
for i in a:
    print (i,i)'''
