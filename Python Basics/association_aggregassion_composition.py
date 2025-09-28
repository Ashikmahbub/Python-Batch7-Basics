#Association, Aggregation, Composition in Python


# Association: A general relationship where one class uses another class.
class Engine:
    def start(self):
        return "Engine started"         
    def stop(self):
        return "Engine stopped"
class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()  # Car uses Engine (Association)
    def start_car(self):
        return self.engine.start()
    def stop_car(self):
        return self.engine.stop()
    
    
my_car = Car("Toyota")
print(my_car.start_car())  # Output: Engine started

print(my_car.stop_car())   # Output: Engine stopped
# Aggregation: A specialized form of association where one class contains a reference to another class.
class Department:
    def __init__(self, name):
        self.name = name        
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []  # University has multiple Departments (Aggregation)
    def add_department(self, department):
        self.departments.append(department)         
        
        
uni = University("ABC University")
cs_dept = Department("Computer Science")
math_dept = Department("Mathematics")
uni.add_department(cs_dept)
uni.add_department(math_dept)   

print(f"University: {uni.name}")
for dept in uni.departments:
    print(f"Department: {dept.name}")
# Output:
# University: ABC University        

# Department: Computer Science
# Department: Mathematics
# Composition: A strong form of aggregation where the contained class cannot exist independently of the container class.
class House:    
    def __init__(self, address):        
        self.address = address
        self.rooms = []  # House contains Rooms (Composition)
    def add_room(self, room):                                   
        
        self.rooms.append(room)
class Room:
    def __init__(self, name):
        self.name = name            
        
house = House("123 Main St")
living_room = Room("Living Room")   
kitchen = Room("Kitchen")
house.add_room(living_room)
house.add_room(kitchen) 

print(f"House Address: {house.address}")
for room in house.rooms:
    print(f"Room: {room.name}") 
# Output:
# House Address: 123 Main St    
# Room: Living Room
# Room: Kitchen 

