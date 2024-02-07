class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = int(input("Please enter length of the rectangle: "))

width = int(input("Please enter width of the rectangle: "))

rec1 = Rectangle(length, width)

print(rec1.area())