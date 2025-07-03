class Shape:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")


# Example usage:
circle = Circle("red", 76)
square = Square("blue", 4)

print_area(circle)  # Output: The area of the shape is: 78.53975
print_area(square)  # Output: The area of the shape is: 16
