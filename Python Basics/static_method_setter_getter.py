# class College:
#     college_name = "ABC College"

#     @staticmethod
#     def college_info():
#         return f"Welcome to {College.college_name}!"
#     def calculate_tuition(fees, semesters):
#         return fees * semesters
    
# print(College.college_info())  # Output: Welcome to ABC College!
# print(College.calculate_tuition(5000, 2))  # Output: 100


class Employee:
    company = "TechCorp"
    
    def __init__(self,name = None, salary = None, age = None):
        self.name = None
        self.age = None 
        self._salary = None #protected variable by convention   but still accessible
    
    @staticmethod
    def company_info():
        return f"Company Name: {Employee.company}"
    @staticmethod
    def calculate_bonus(salary, bonus_percentage):
        return salary * (bonus_percentage / 100)
    
    
    def get_salary(self,password):
        if password == "admin123":
            return self._salary
        else:
            return "Access Denied"
        
    def set_salary(self, password, salary):
        if password == "admin123":
            self._salary = salary
        else:
            
            print("Access Denied")
        
    
Emp1 = Employee("Alice", 70000, 30)
Emp2 = Employee( "Bob", 60000, 25) 

Emp1._salary = 80000
print(Emp1.company_info())  # Output: Company Name: TechCorp
print(Emp2.company_info())  # Output: Company Name: TechCorp    



print(Emp1.get_salary("admin123"))#
Emp2.set_salary("admin123", 90000)
print(Emp2.get_salary("admin123"))#




print(Employee.company_info())  # Output: Company Name: TechCorp
print(Employee.company_info())  # Output: Company Name: TechCorp