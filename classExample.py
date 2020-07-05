class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("George", 23)
p1.myfunc()

#from w3schools.com:

#   the self parameter is a reference to the current instance of the class, 
#   and is used to access variables that belong to the class
#
#   the "self" parameter does not need to be named "self", you 
#   can call it whatever you like, but it has to be the first
#   parameter of any function in the class. 

class Box:
    #the __init__ function is called automatically everytime
    #the class is being used to create a new object, and thus
    #is like a standard constructor. 
    def __init__(stupidBox, length, width):
        stupidBox.length = length
        stupidBox.width = width
    def getWid(stupidBox):
        return stupidBox.width

    #can come up with different name for the 'self' param
    def getLen(reallyStupidBox):
        return reallyStupidBox.length

box1 = Box(14,12)
print('The length of box1 is: ' + str(box1.getLen()))
print('The width of box1 is: ' + str(box1.getWid()))

#modify object properties
box1.length = 15
print('The length of box1 is now : ' + str(box1.getLen()))

#delete object properties
del box1.width

#this code gives an error when running
#print('The length of box1 is: ' + str(box1.getWid()))

#this is how you would delete an object
del box1

#the pass statement allows you to define an empty class:
#the pass statement is necessary if you want to have no content
class vehicle:
    pass


