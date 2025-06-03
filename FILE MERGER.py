def create_file():
    filename1 = input("Filename 1: ")
    file1 = open(filename1,'w')
    while True:
        text1 = input("Enter text: ")
        file1.write(text1 + '\n')
        ch = input("Do you wish to add more text? (y/n) ")
        if ch == 'n':
            break
    print("File 1 sucessfully created")
    print()
    filename2 = input("Filename 2: ")
    file2 = open(filename2,'w')
    while True:
        text2 = input("Enter text: ")
        file2.write(text2 + '\n')
        ch = input("Do you wish to add more text? (y/n) ")
        if ch == 'n':
            break
    print("File 2 sucessfully created")
    print()    
    file1.close()
    file2.close()
    file3(filename1,filename2)
    
def file3(filename1,filename2):
    f1 = open(filename1)
    f2 = open(filename2)
    filename3 = input("Enter filename for the new file to be created: ")
    file3 = open(filename3,'w')
    for i in f1.readlines():
        file3.write(i)
    for j in f2.readlines():
        file3.write(j)
    file3.close()

create_file()
print("File successfully created")
