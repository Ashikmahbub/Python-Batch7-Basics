#Hierarchical Inheritance is a type of inheritance in which multiple derived classes inherit from a single base class.
class Animal:           #base class
    def speak(self):
        print("Animal speaks")  
class Dog(Animal):      #derived class 1
    def bark(self):
        print("Dog barks")
class Cat(Animal):      #derived class 2
    def meow(self):
        print("Cat meows")
class Cow(Animal):      #derived class 3
    def moo(self):
        print("Cow moos")

dog = Dog()
dog.speak()  #inherited method from Animal class
dog.bark()   #method from Dog class
cat = Cat()
cat.speak()  #inherited method from Animal class
cat.meow()   #method from Cat class
cow = Cow()
cow.speak()  #inherited method from Animal class
cow.moo()    #method from Cow class
#Hierarchical Inheritance
#hybrid inheritance is a combination of two or more types of inheritance.   

#Hybrid Inheritance 

class A:               #base class
    def method_a(self):
        print("Method A from class A")
class B(A):            #derived class 1
    def method_b(self):
        print("Method B from class B")
class C(A):            #derived class 2
    def method_c(self):
        print("Method C from class C")
class D(B, C):         #derived class 3
    def method_d(self):
        print("Method D from class D")
d = D()
d.method_a()  #inherited method from class A
d.method_b()  #inherited method from class B    
d.method_c()  #inherited method from class C

d.method_d()  #method from class D
#Hybrid Inheritance is a combination of two or more types of inheritance.