# # #classes n objects
# # class myclass:
# #     x=5
# # p1=myclass() #creating the object 
# # print(p1.x)  #accessing the attribute

# # #example
# # class Dog:
#     #a simple class
#     #attributes
# #     attr1 ="mammal"
# #     attr2="dog"

# # # # Driver code
# # # # object  instantaneous
# # # Rodger= Dog()    
# # # print(Rodger.attr1)
# # # print(Rodger.attr2)

# # #create a class named person, use the__init__()function to assign values for names and age:




# # class Person:
# #     def __init__(me, name,age):
# #        me.name=name
# #        me.age=age   
# # person=Person("john",1000)
# # print(person.name)


# #object method
# #insert afunction thats print agreeting ,and execute it on the on the p1 object:
# class person:
#     def __init__(self,name,age):
#         self.name =name
#         self.age=age
#     def myfunc(self):
#         print("hello my name is "+self.name)  
# p1 =person("john",36)  
# p1.myfunc()
#
# class person:
#     def __init__(self,name,age):
#         self.name =name
#         self.age=age
#     def myfunc(self):
#         print("hello my name is "+self.name)  
# p1 =person("john",36)  
# p1.myfunc()
# p1.age=800
# print("i have done"+ str(p1.age)+"videos")
# del p1

#class and instance and variable

class jkl:
    #class variable
    animal ='dog'
    #The init method or constructor
    # 
    # def __init__(self, breed,color):
    #     #instance variable
    #     self.breed=breed
    #     self.color=color
    # # objeccts in dog class
    # Rodger =Dog("Pull","brown")  
    # buzo =Dog("bulldog","black")

    # class variable
animal ="dog"
#the init method or contructor
def __init__(self,breed):
   #instance variable
   self.breed =breed
#adds  on instance variable
def setcolor(self,color):
   self.color=color
#retrieves instance varaible
def getcolor(self):
   return self.color
#driver code
Rodger = jkl("pug")
Rodger.setcolor("brown")  
print(Rodger.getcolor())   
   

