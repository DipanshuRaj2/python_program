sum=0
print('enter the value of m and n and take m smaller than n')
m=int(input('value of m'))
n=int(input('value of n'))
for i in range(m,n):
    sum=sum+i
avg=sum/(n-m)
print(sum)
print(avg)