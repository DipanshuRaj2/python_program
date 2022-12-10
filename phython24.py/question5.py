#**********wap to display between m to n .
print('enter the no.which m  greater then n')
m=int(input("enter the number of m "))
n=int(input("enter the number of n "))
count=0
for i in range(m,n+1):
    if(i%2==0):
        print(i)
        count=(count+1)
print("total even no. " ,count)    


    