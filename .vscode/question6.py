year=int(input("enter your year"))
if(year%4==0 and year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("this is not a leap year")