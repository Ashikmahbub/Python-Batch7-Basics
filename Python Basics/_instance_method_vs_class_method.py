class Employee:
    
    company = "TechCorp"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #instance method to display instance variables
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    #class method to change class variable
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        
        
# Creating instances of the Employee class
emp1 = Employee("Alice", 30)
emp2 = Employee("Bob", 25)

print(emp1.display_info())  # Output: Name: Alice, Age: 30
print(emp2.display_info())  # Output: Name: Bob, Age: 25
print(emp1.company)  # Output: TechCorp
print(emp2.company)  # Output: TechCorp
# Changing the company using class method
Employee.change_company("InnoTech")
print(emp1.company)  # Output: InnoTech
print(emp2.company)  # Output: InnoTech