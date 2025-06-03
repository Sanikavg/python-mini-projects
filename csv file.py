import csv

def add():
    bookid = int(input("Book ID: "))
    bookname = input("Book Name: ")
    author = input("Author: ")
    price = float(input("Price: "))
    with open("books.csv", 'a' , newline='') as f:
        csv_w = csv.writer(f)
        csv_w.writerow([bookid,bookname,author,price])

def search():
    bookname = input("Enter bookname: ")
    with open("books.csv", 'r', newline='') as f:
        csv_w = csv.reader(f)
        for i in csv_w:
            if i[1] == bookname:
                print("Bookid: %s\n Bookname: %s\n Author:%s\n Price:%s\n"%(i[0],i[1],i[2],i[3]))
                break
        else:
            print("Book not found")

def display():
    with open("books.csv",'r') as f:
        robj = csv.reader(f)
        for i in robj:
            print('%s\t%s\t%\t%s\t'%(i[0],i[1],i[2],i[3]))

def modify():
    n=[]
    with open("books.csv",'r') as f:
        robj = csv.reader(f)
        for i in robj:
            n.append(i)
        bname = input("Enter book name to be modified: ")
        bookid = int(input("BookID: "))
        bookname = input("Book Name: ")
        author = input("Author: ")
        price = int(input("price: "))
        md = [bookid, bookname, author,price]
        for i in n:
            if n[i][1] == bname:
                n[i] = md
                break
        else:
            print("book not found")
        with open("books.csv",'w',newline='') as f1:
            wobj=csv.writer(f1)
            wobj.writerows(n)
            
              
    
        
