try:
   '''fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")'''
   a=open("xy","x")
   a.write("hello")
except IOError:
   
   print ("Error: can\'t find file or read data")
else:
   print( "Written content in the file successfully")
   fh.close(a)
