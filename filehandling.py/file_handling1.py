#open function is used to reading and writing file
#open the file .txt in Read mode

#read line means only read 1 line

fileptr = open("file.txt","r")
'''if fileptr
    print("file is open successfully")'''
with open ("C:\Users\dipan\OneDrive\Desktop\python\filehandling.py\file.txt",'r') as f:
    content = f.read()
    print (content)

fileptr.close()
