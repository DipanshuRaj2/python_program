#Write into a file
# file does not exist

fp =open("file2.txt" , "w")

fp.write("text")

with open("file2.txt","r") as fp:
    con = fp.read()
    print(con)
fp.close()