# Write a Simple code for multilevel Inheritance

# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Intermediate class
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

# Derived class
class GraduateStudent(Student):
    def __init__(self, name, student_id, course):
        super().__init__(name, student_id)
        self.course = course
        
grad_student = GraduateStudent("sammy", "122", "sce")
print(grad_student.name)        
print(grad_student.student_id)    
print(grad_student.course)  
