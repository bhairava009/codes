class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def get_result(self):
        return "Pass" if self.marks >= 40 else "Fail"

# funtions
student1 = Student("ram", 1, 85)
student2 = Student("ravi", 2, 30)
student3 = Student("Champa", 3, 50)
print(f"{student1.name} (Roll: {student1.roll}): {student1.get_result()}") 
print(f"{student2.name} (Roll: {student2.roll}): {student2.get_result()}")  
print(f"{student3.name} (Roll: {student3.roll}): {student3.get_result()}") 
