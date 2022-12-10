amount = int(input('Enter your amount'))
if amount < 150000:
    print("no pay tax")
elif (amount >150001) and (amount<=300000):
    tax=(amount*10)/100
    print("10% pay tax", tax)
elif (amount >300001) and (amount<=500000):
    tax=(amount*20)/100
    print("20% pay tax", tax)
else:
    tax=(amount*30)/100
    print("30% pay tax" ,tax)
