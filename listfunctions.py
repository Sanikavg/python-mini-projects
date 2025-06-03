a="hello5"
b="1234"
c="hi"
print(a.isdigit())
print(b.isdigit())
print(c.isalpha())

l=['a','b','a','c','c']
#to remove duplicates from list
l.sort()
print(l)
l.sort(reverse=True)
print(l)
x=list(dict.fromkeys(l))
print(x)
