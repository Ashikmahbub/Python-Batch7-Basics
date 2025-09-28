#Builder Design Pattern Example in Python 


class Car:   
    def __init__(self):
        self.parts = []
    def add_part(self, part):
        self.parts.append(part) 
    def show_parts(self):
        return "Car parts: " + ", ".join(self.parts)    
class CarBuilder:   
    def __init__(self):
        self.car = Car()
    def add_wheels(self):
        self.car.add_part("Wheels")
        return self
    def add_engine(self):
        self.car.add_part("Engine")
        return self

    def add_body(self):
        self.car.add_part("Body")
        return self
    def get_car(self):
        return self.car
# Director
class CarDirector:
    def __init__(self, builder):
        self.builder = builder
    def construct_sports_car(self):
        return (self.builder.add_wheels()
                            .add_engine()
                            .add_body()
                            .get_car())
    def construct_economy_car(self):
        return (self.builder.add_wheels()
                            .add_body()
                            .get_car())
# Usage
builder = CarBuilder()
director = CarDirector(builder)
sports_car = director.construct_sports_car()
print(sports_car.show_parts())  # Output: Car parts: Wheels, Engine, Body
economy_car = director.construct_economy_car()
print(economy_car.show_parts())  # Output: Car parts: Wheels, Body