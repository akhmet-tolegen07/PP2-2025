class Shape:
    def area(self):
        print("The area of shape: ", 0)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  
        self.width = width    

    def area(self):
        print("The area of rectangle: ", self.length * self.width) 


rectangle = Rectangle(43, 62)
rectangle.area() 
