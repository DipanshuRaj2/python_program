# ****write a program to calculate the factorial of a number*****
n=int(input("enter the number: "))
fact=1
if(n==0):
    print(fact)
else:
    while(n>0):
        fact=fact*n
        n=n-1
    print(fact)    

