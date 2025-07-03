
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def show_details(self):
        return (super().show_details() +  f", Roll Number: {self.roll_number}")
    
student = Student("Ram", 20, "01")

print(student.show_details())
    