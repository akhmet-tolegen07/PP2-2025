import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("The coordinates of the point: ", self.x, self.y)

    def move(self, newx, newy):
        self.x = newx
        self.y = newy
        print("Point moved to: ", self.x,  self.y)

    def dist(self, second_point):
        d = math.sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2)
        print("The distance between 2 points: ", d)
        return d

p1 = Point(3, 6)
p2 = Point(5, 7)

p1.show()
p1.move(5, 10)
p1.dist(p2)
