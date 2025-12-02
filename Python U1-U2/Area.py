class Shape:
    def area(self):
        print("Area of shape is not defined.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


c = Circle(5)
r = Rectangle(4, 6)
s = Shape()


print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
s.area()
