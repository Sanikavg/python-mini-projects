a={1:'a',2:'b',3:'c'}
b={}
for i in a.values():
    print(i)
for i,j in a.items():
    print(i,j)

print(a[3])
a[4]='d'#add element
a[3]='e'#change element
a.pop(3)#function
a.popitem()
print(a)
del a[1]#keyword
del a#to delete entire dict
a.clear()
b=a.copy()
#or
b=dict(a)
a.update({5:'f'})#add element function
c=a.get(2)
