#WAP to print whether the given numberis armstrong or not?*****
n=int(input("enter your number "))
order=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if n==sum:
    print(n,"is an armstong number")
else:
    print(n,"is not an armsstrong number")
