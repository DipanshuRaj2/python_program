# ************wap to display the reverse of a number.*****
n=int(input("enter your number "))
rev=0
while(n!=0):
    t=n%10
    rev=rev*10+t
    n=n//10
print(rev)