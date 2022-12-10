print("enter any +ve nos.and -1 to exit")
n=int(input("enter the no. "))
sum=0
count=0
while(n!=-1):
    sum=sum+n
    n=int(input("enter any no."))
    count = count + 1
print(sum)
avg=sum/count
print(avg)
#wap to calculate sum and average of n random nos.