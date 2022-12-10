n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))
if n1>n2 and n1>n3:
    print("first no. is greater")
elif n2>n1 and n2>n3:
    print("second no. is greater")
else:
    print("third no. is greater")