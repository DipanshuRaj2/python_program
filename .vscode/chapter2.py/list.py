# #list is mutable value  and it is ordered sequence
# # []

# lst=[1,2,3,4,5]
# b = type(lst)
# print(b ,lst)

# #slicing ,concatenation,indexing 
fib=[1,1,2,3,5,8,13,21]
# fib[4] #indexing
# print(fib[4] ,fib[6]) #13


# #slicing
print(fib[2:6])
# # print(fib[-6:-1])
# #concatenation 
# # l1=[1,2,3]
# # l2=[4,5,6]
# # l1+l2
# # print(l1+l2)
# # print([0]+fib)

# #nested list
# l1=[20,25,30]
# # l2=[5,10,15,l1]
# # print(l2)
# # l1=[20,25,30]
# # print(l1)
# # l1[1]=38
# # print(l1)

# #reptition
# print(3*l1)

# unpacking
# x1,x2,x3=[11,22,33]
# print(x1,x2,x3)

# append function used in list
#append=()add a single to the list
# odd=[1,3,5]
# odd.append(7) 
# print(odd)
# #extend
# odd.extend([9,11,13])
# print(odd)

# #insert
# odd.insert(1,78)
# print(odd)
#delete
# del odd[1]
# print(odd)
#delete multiple items
# del odd[1:2]
# print(odd)
# # insert remove
# odd=[1,3,5,7,9,11]
# odd.remove(3)
# print(odd)
# #insert pop
# odd.pop(4)
# print(odd)