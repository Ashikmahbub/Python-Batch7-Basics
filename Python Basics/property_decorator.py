class Employee:
    company = "TechCorp"

    def __init__(self, name=None, salary=None, age=None):
        self.name = name
        self.age = age
        self.__salary = salary  # private variable

    @staticmethod
    def company_info():
        return f"Company Name: {Employee.company}"

    @staticmethod
    def calculate_bonus(salary, bonus_percentage):
        return salary * (bonus_percentage / 100)

    # Getter only (no setter)
    @property
    def salary(self):
        return self.__salary

    # Optional: controlled method to change salary
    def update_salary(self, password, new_salary):
        if password == "admin123":
            self.__salary = new_salary
        else:
            print("Access Denied")


# Usage
Emp1 = Employee("Alice", 70000, 30)
Emp2 = Employee("Bob", 60000, 25)

print(Emp1.salary)  # 70000
print(Emp2.salary)  # 60000

# Trying to change salary directly will fail
Emp1.salary = 80000  # ERROR: AttributeError: can't set attribute

# Correct way: controlled update
# Emp1.update_salary("wrongpass", 80000)  # Access Denied
# Emp1.update_salary("admin123", 80000)   # Works
print(Emp1.salary)                       # 80000
