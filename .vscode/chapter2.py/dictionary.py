#phython dictionary is an unordered collection of items.
#each item has of adictionary has akey /value pair.
#we use culy braces {}
#kkey value =(key:value) 

#empty dictionary 
my_dict={}
print(my_dict)
#dictionary with integer keys
# my_dict={1:'apple',2:'ball'}
# print(my_dict)
# #dictionary with mixed key
# my_dict={'name':'john',1:[2,8,7]}
# print(my_dict)

# #using dict()
# my_dict=dict({1:'apple',2:'ball'})
# print(my_dict)
# #from sequence having each item is a pair
# my_dict=dict([(1,'apple'),(2,'ball')])
# print=my_dict
# 1.get() -it gives null rather than error 
#2.key[]-it gives a key error

#get vs [] for retriving elements
# my_dict={'name':'jack','age':26}
# #output jack
# print(my_dict['name'])
# #output :26
# print(my_dict.get('age'))
# #trying to access the keys which doesn't exits throws error 
# #output none 
# print(my_dict.get('address'))
# #key error
# print(my_dict['address'])

# #changing and adding dictionary elements 
# my_dict ={'name':'jack','age':26}
# #update value 
# my_dict['age']=27
# #output:{'age':27,'name':'jack'}
# print(my_dict)
# #add item
# my_dict['address']='Downtown'
# #output:{'address':''downtown', 'age':27,'name':'jack'}
# print(my_dict)

#removing elements from a dictionary
#create a dictionary
squares={1:1, 2:4, 3:9,4:16,5:25}

#remove a particular item . returns its value
#output:16
print(squares.pop(4))
#output:{1:1,2:4,3:9,5:25}
print(squares)
#remove an arbitiary item .return (key value)
#output:(5,25)
print(squares.popitem())

#output:{1:1,2:4,3:9}
print(squares)

#remove all item
squares.clear()
#output :{}
print(squares)
#delete the dictinary itself
del squares

#throws error
print(squares)


