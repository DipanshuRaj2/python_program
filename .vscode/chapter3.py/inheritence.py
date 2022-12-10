#inheritence=we don't change the base class
#we create the base class as child class
#

#example 1
# class Animal:
#     def speak(self):
#         print("Animal Speaking")
#         #child class dog inherits the base class animals
# class Dog(Animal):
#     def bark (self):
#         print("dog barking")
# d=Dog()
# d.bark()
# d.speak()
#types of inheritance


# 1.multi level inheritance  
#example
# class Animal:
#     def speak(self):
#         print("Animal Speaking")
#         #child class dog inherits the base class animals
# class Dog(Animal):
#     def bark (self):
#         print("dog barking")
# #The child class Dog child inherits another child class Dog
# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread...")

# d=DogChild()
# d.bark()
# d.speak()
# d.eat()


#2. multiple inheritance  
#example
# class calculation1:
#     def Summation(self,a,b):
#         return a+b;
# class calculation2:
#     def Multiplication(self,a,b):
#         return a*b;
# class Derived(calculation1,calculation2):
#     def Divide(self,a,b):
#         return a/b;
# d = Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))

#       issubclass
class calculation1:
    def Summation(self,a,b):
        return a+b;
class calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(calculation1,calculation2):
    def Divide(self,a,b):
        return a/b;
d =Derived()
print(issubclass(Derived,calculation2))
print(issubclass(calculation1,calculation2))

# isinstance(obj,class)method
#the isinstance()method is used to check the relationship between the object and class.
#It return true if the first parameter i.e obj is the instance of the second parameter i.e
# class
print(isinstance(d, Derived))




#Create a class building having properties like name , area.create another class apartment
#inheriting the properties of building .also creates 2 instances of it









