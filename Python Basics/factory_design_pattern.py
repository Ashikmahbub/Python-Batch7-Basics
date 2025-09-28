#factory
class Car:
    def info(self):
        return "This is a car."
class Bike:
    def info(self):
        return "This is a bike."
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle type")
 
car = VehicleFactory.get_vehicle("car")
print(car.info())  # Output: This is a car.