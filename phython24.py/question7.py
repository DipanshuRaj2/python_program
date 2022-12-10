# *****wap to calculate the sum of a number*****
n=int(input("enter your number"))
sum=0
while(n!=0):
    t=n%10
    sum=sum+t   
    n=n//10
print(sum)