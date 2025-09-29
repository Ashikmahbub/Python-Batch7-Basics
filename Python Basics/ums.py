class  Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."
    
class Student(Person):
    def __init__(self, name, age, student_id, course_list,gpa):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list = []
        
        self.__gpa = gpa
        self.gpa = gpa
        

    def introduce(self):
        base_introduction = super().introduce()
        return f"{base_introduction} My student ID is {self.student_id}."
    
    def enroll(self, course):
        self.course_list.append(course)
        return f"{self.name} has enrolled in {course}."
    
    @property
    def gpa(self)->float:
        return self.__gpa
    
    @gpa.setter
    def gpa(self,value:float):
        value = float(value)
        if not (0.0 <= value <= 4):
            raise ValueError("GPA must be between 0.0 and 4.0")
        
        self.__gpa = value
        
        
    @staticmethod
    def is_valid_id(student_id:str):
        rtetun
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        
        self.subject =subject 
        def introduce(self):
            return f"I am professor {self.name} and I teach {self.subject}."
 
    
    def assign_subject(self, subject):
         
        return f"{self.name} has been assigned to teach {subject}."