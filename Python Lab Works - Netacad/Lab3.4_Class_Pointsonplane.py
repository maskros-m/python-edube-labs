import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x1 = x
        self.__y1 = y

    def getx(self):
        return self.__x1

    def gety(self):
        return self.__y1

    def distance_from_xy(self, x, y):
        self.__x2 = x
        self.__y2 = y
        
        self.__perpendicular = abs(self.__y2 - self.__y1)
        self.__base = abs(self.__x2 - self.__x1)
        
        self.__distance = math.hypot(self.__perpendicular, self.__base)
        
        return self.__distance

    def distance_from_point(self, point):
        self.__x2 = point.getx()
        self.__y2 = point.gety()
        
        self.__perpendicular = abs(self.__y2 - self.__y1)
        self.__base = abs(self.__x2 - self.__x1)
        
        self.__distance = math.hypot(self.__perpendicular, self.__base)
        
        return self.__distance


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
