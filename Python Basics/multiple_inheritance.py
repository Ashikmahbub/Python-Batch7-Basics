
#Multiple inhereitance in python is a feature that allows a class (derived class) to inherit attributes and methods from more than one base class (parent classes). This enables the derived class to combine functionalities from multiple sources, promoting code reusability and flexibility.
#Multiple Inheritance

class Base1:
    def feature1(self):
        print("Feature 1 from Base1")
    
    def feature2(self):
        print("Feature 2 from Base1")       
class Base2:
    def feature3(self):
        print("Feature 3 from Base2")
    
    def feature4(self):
        print("Feature 4 from Base2")
class Derived(Base1, Base2):
    def feature5(self):
        print("Feature 5 from Derived") 
d = Derived()
d.feature1()  # Inherited from Base1
d.feature3()  # Inherited from Base2
d.feature5()  # Defined in Derived

#Multilevel Inheritance in python is a type of inheritance where a class (derived class) 
# inherits from another class (base class), which in turn inherits from another class (grandparent class). 
# This creates a multi-level hierarchy of classes,
# allowing the derived class to inherit attributes and methods from both its parent and grandparent classes.

class Grandparent:  
    
    def feature1(self):
        print("Feature 1 from Grandparent")
    
    def feature2(self):
        print("Feature 2 from Grandparent") 
class Parent(Grandparent):
    def feature3(self):
        print("Feature 3 from Parent")
    
    def feature4(self):
        print("Feature 4 from Parent")
class Child(Parent):
    def feature5(self):
        print("Feature 5 from Child")
        