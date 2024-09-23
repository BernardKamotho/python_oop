# This is the aspect of an element taking different forms.
# poly == many
# morphes == forms

class Shape:
    def __init__(self, width):
        self.width = width
    
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width)
        self.height = height

    def area(self):
        return self.width * self.height * 0.5

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return  self.radius**2 * 3.14


triangle = Triangle(4, 2)
cicle = Circle(7)
print("The area of the triangle is:", triangle.area())
print("The area of the circle is:", cicle.area())