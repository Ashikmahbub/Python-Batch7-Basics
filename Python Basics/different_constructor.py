class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
    def __init__(self,brand = "Toyota", model = "X corolla", year = 2020):
        self.make = brand
        self.model = model
        self.year = year

    def display_info(self):
         return f"{self.year} {self.make} {self.model}"
my_car = Car("Toyota", "Camry", 2020)
his_car = Car(2019, "Civic", "Honda")
my_car.make = "Honda"
print(my_car.display_info())


#Default constructor
default_car = Car()
print(default_car.display_info())