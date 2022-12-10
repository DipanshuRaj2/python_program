#example of a recursive function
def factorial(x):
    """This is a recursive function to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))
    
num =int(input("Enter the number:- "))
print("the factorial of ",num, "is",factorial(num))