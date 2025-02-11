import math


class Line:
    def __init__(self,coord1,coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return (y2 - y1)/(x2 - x1)

    def __str__(self):
        return f'Line with coordinates ({self.coord1[0]},{self.coord1[1]}) ({self.coord2[0]},{self.coord2[1]}) '

class Cylinder:

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return (2 * math.pi * (self.radius ** 2)) + (2 * math.pi * self.radius * self.height)


if __name__ == '__main__':
    line = Line((3,2),(8,10))
    print(f'Distance of {line} is {line.distance()}')
    print(f'Slope of {line} is {line.slope()}')

    cylinder = Cylinder(2,3)
    print(f'Volume is {cylinder.volume()}')
    print(f'Surface area is {cylinder.surface_area()}')
