class School:
    # Class variable
    school_name = "ABC High School"

    def __init__(self, student_name, student_age):
        # Instance variables
        self.student_name = student_name
        self.student_age = student_age
        
    def display_info(self):
        return f"Student Name: {self.student_name}, Age: {self.student_age}, School: {School.school_name}"
# Creating instances of the School class

sc1 = School("Alice", 14)
sc2 = School("Bob", 15)

print(sc1.display_info())  # Output: Student Name: Alice, Age: 14, School: ABC High School
print(sc2.display_info())  # Output: Student Name: Bob, Age: 15

sc2.school_name = "XYZ High School"  # This creates an instance variable, does not change class variable
print(sc1.display_info())  # Output: Student Name: Alice, Age: 14

School.school_name = "XYZ High School"  # Changing the class variable
print(sc1.display_info())  # Output: Student Name: Alice, Age: 14, School: XYZ High School
print(sc2.display_info())  # Output: Student Name: Bob, Age: 15, School: XYZ High School