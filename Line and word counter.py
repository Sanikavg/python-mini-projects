def file_create():
    filename = input("filename: ")
    file = open(filename, 'w')
    text = input("Enter text: ")
    file.write(text)
    file.close()
    count(filename)
def count(filename):
    file = open(filename, 'r')
    count_l =0
    count_w = 0
    for i in file.readlines():
        count_l += 1
        for j in i.split():
            count_w += 1
    if count_l == 0:
        print("File is empty")
    else:
        print("Count of words: ",count_w)
        print("Count of lines: ",count_l)
    file.close()

file_create()
