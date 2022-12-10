print('Enter your choice')
print('car')
print('bus')
print('cycle')
choice = input()

c = 'car'
b = 'bus'
o = 'cycle'


time = int(input("Enter time of parking in hour"))

if choice == c:
    price = time * 10
    print("your cost of parking", price)
elif choice == b:
    price = time * 20
    print("your cost of parking", price)
elif choice == o:
    price = time * 5
    print("your cost of parking", price)
else:
    print("servie is not avaliable")


