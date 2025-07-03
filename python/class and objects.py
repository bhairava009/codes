# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             return "Error: Division by zero"
#         return a / b
# calc = Calculator()


# print("Addition:", calc.add(5, 3))       
# print("Subtraction:", calc.subtract(5, 3))  
# print("Multiplication:", calc.multiply(5, 3)) 
# print("Division:", calc.divide(5, 3))        
# print("Division by zero:", calc.divide(5, 0))


class rectangle:
    def__init__(self,length, width)
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = rectangle(5, 3)
print("Area of rectangle:", rect.area())

print("Perimeter of rectangle:", rect.perimeter())
