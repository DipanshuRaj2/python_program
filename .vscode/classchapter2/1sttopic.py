# # def simple():
# #     print("hello!")
# # print("outside function") 
# # simple()


# #wap to calculate sum of2 no. using function
# # def add():
# #     print(a+b)
# # a=int(input("enter your value:-")) 
# # # b=int(input("enter your second no:-"))  
# # # add()

# # #wap to calculate sum and averge of first n natural no. using function with parameters. 



# # def sum_avg(n: int):
# #     sum = 0
# #     i = 0
# #     while(n <= i):
# #         sum = sum + i
# #         avg = avg / n
# #     print(sum)
# #     print(avg)
# # n = int(input("enter your number"))
# # sum_avg(n)
# # def sum_avg(n:int):
# #     sum=0
# #     for i in range(1,n+1):
# #         sum=sum+i
# #     print("sum is" , sum)
# #     avg=sum/n
# #     print("average is", avg)
# # n=int(input("enter the value of n"))
# # sum_avg(n)    

# # sum of natural no.
# def n_sum(n:int):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     return sum
# n=int(input("enter the value of n"))  
# ans=n_sum(n)
# print("sum is", ans)   

def even_odd(n:int)->str:
    if(n%2==0):
        print(str("number is even"))
    else:
        print(str("number is odd"))
    return str
n=int(input("enter the number"))            
even_odd(n)



  