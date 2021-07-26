class Point:
    def __init__(self, x, y):
        self.coordX = x
        self.coordY = y
        
    def print(self):
        print(str(self.x) + ',' + str(self.y))


class Rectangle:
    def __init__(self, start_point, width, height):
        self.start_point = start_point
        self.width = width
        self.high = height

    def get_area(self):
        return self.width * self.height
    
    def get_start_point(self):
        return self.start_point

    def get_end_point(self):
        end_point_x = self.start_point.x + self.width
        end_point_y = self.start_point.y + self.height
        return Point(end_point_x, end_point_y)


def create_rectangle():
    origin = Point(50, 100)
    return Rectangle(origin, 90, 10)

my_rect = create_rectangle()
print('Starting Point: ' + my_rect.get_start_point.print())
print('Ending Point: ' + my_rect.get_end_point.print())
print('Area: ' + my_rect.get_area())
