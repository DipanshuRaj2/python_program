'''
OOP = Object Oriented Programming
1.It is the programming paradigm that uses objects and classes in programming. 
2.It helps to implement real world entities.
3.The main concept of OOps is to bind the data
 and the function that work together in the single unit .

ex= Suppose if we have 100 value in the different types that is we take
as example of dogs if we find the any certain dog, we have to know the 
index number of the dog so that it's not good things that is to remember 
every index or count the index so the concept OOPs is make.

then what we have to do
we create a class and object in the programming then we have to access
the any element in the program . 


'''
#Creating a class and object with class and instance attributes

class Dog:

    #class attribute
    attr1 = "mammal"

    #Instance attribute'
    def __init__(self,name):
        self.name = name

# Driver code
# object instantiation
Rodger = Dog('Rodger')
Tommy = Dog('Tommy')

#Accessing class attributes
print('Rodger is a {}'.format(Rodger.__class__.attr1))
print('Tommy is also a {}'.format(Tommy.__class__.attr1))

#Accessing instance attributes
print('My name is{}'.format(Rodger.name))
print('My name is{}'.format(Tommy.name))

###################################################

#Creating Class and objects with methods

class Dog:
    #class attribute
    attr1 ='mammal'

    #Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('My name is {}'.format(self.name))

# Driver code
# Object instantation

Rodger = Dog('Rodger')
Tommy = Dog('Tommy')          

# Accessing class methods
Rodger.speak()
Tommy.speak()