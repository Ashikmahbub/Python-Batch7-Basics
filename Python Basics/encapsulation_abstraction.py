#encapsulatipn and abstraction in python
#Encapsulation is a fundamental concept in object-oriented programming that restricts direct access to an object's data and methods.
# It is achieved by bundling the data (attributes) and methods (functions) that operate on the data into a single unit, typically a class.
#Encapsulation helps in protecting the internal state of an object from unintended interference and misuse, promoting data integrity and security. 
#Abstraction, on the other hand, is the process of simplifying complex systems by hiding unnecessary details and exposing only the essential features.
# It allows programmers to focus on high-level operations without getting bogged down by low-level implementation details.
#Abstraction is often achieved through abstract classes and interfaces, which define a contract for subclasses to
class Grandparent:  
    
    def feature1(self):
        print("Feature 1 from Grandparent")
    
    def feature2(self):
        print("Feature 2 from Grandparent") 
    def __feature3(self):  # Private method
        print("Feature 3 from Grandparent (Private)")
        
class Parent(Grandparent):
    def feature4(self):
        print("Feature 4 from Parent")
    
    def feature5(self):
        print("Feature 5 from Parent")
    def access_private_feature(self):
        self._Grandparent__feature3()  # Accessing private method from Grandparent
        
class Child(Parent):
    def feature6(self):
        print("Feature 6 from Child")
    def access_grandparent_private_feature(self):
        self._Grandparent__feature3()  # Accessing private method from Grandparent through Parent   
 


c = Child()
c.feature1()  # Inherited from Grandparent
c.feature4()  # Inherited from Parent
c.feature6()  # Defined in Child
c.access_private_feature()  # Accessing private method from Grandparent through Parent
c.access_grandparent_private_feature()  # Accessing private method from Grandparent through Child
#Encapsulation and abstraction are essential principles in object-oriented programming that enhance code organization, maintainability, and security.
# They allow developers to create robust and modular software systems by controlling access to data and simplifying complex interactions.   

#abstraction example
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass        
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
# Usage
dog = Dog()
cat = Cat() 
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow! implement specific behaviors.

