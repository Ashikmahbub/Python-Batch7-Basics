#inheritance in python is a mechanism where a new class (derived class) 
# can inherit attributes and methods from an existing class (base class).
# This promotes code reusability and establishes a hierarchical relationship between classes.

# Base class (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):    
        return "Animal sound" 
class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # Overriding the speak method
        return "Woof!"
    
class Cat(Animal):  # Cat inherits from Animal
    def speak(self):  # Overriding the speak method
        return "Meow!"  
# Creating instances of the derived classes
dog = Dog("Buddy")  
cat = Cat("Whiskers")

print(f"{dog.name} says: {dog.speak()}")  # Output: Buddy says: Woof! 