# a =10
# b=20
# c=sum((a,b)) #built in function
# print(c)

# def function1(a,b):
#     print('Hello you are in function 1', a+b)

# function1(5,7)

'''
def function2(a,b):
    average  = (a+b)/2 
    #print (average)
    return average
v=function2(5,7)
print(v)
'''
##################################
# A simple phython function

def fun():
    print("Welcome to the GFG")
#driver code to call a function
fun()



def add(num1: int, num2: int) -> int:
    """Add two number"""
    num3 = num1 + num2

    return num3

#Driver code
num1 , num2 = 5, 15
ans = add(num1, num2)
print(f'The addition of {num1} and {num2} results {ans}.')
