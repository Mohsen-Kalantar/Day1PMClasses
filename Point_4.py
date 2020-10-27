class Point:
    counter=0 # A class attribute
    def __init__(self, vx, vy):
        self.__x=vx   # attribute x is defined here
        self.__y=vy   # attribute y is defined here
        Point.counter += 1
    def __del__(self):
        Point.counter -= 1
    def __str__(self):
        return f"<{self.__x},{self.__y}>"
    def __add__(self, other):
        return Point(self.__x+other.__x, self.__y+other.__y)
    def distance(self, other):
        import math
        return math.sqrt((other.__x-self.__x)**2 + (other.__y-self.__y)**2)
    def clear(self):
        self.__x=self.__y=0
    def getX(self):
        return self.__x
    def setX(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid attribute value {value}")
        self.__x=value
    x=property(getX, setX)    
    def getY(self):
        return self.__y
    def setY(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid attribute value {value}")
        self.__y=value
    y=property(getY, setY) 


print(f"Counter {Point.counter}")     
p1=Point(0,0)
print(p1.__dict__)
# 1) p1=Point.__new__()
# 2) p1.__init__(0,0) -> __init__(p1,0,0)
p2=Point(2,3)
print(p1.x) # 0
# print(str(p1)) -> print(p1.__str__())
print(p2) # <2,3>
p1.x += 5
print(p1) # <5,0>
p3=p1+p2
print(f"Counter {Point.counter}") 
# # p3=p1.__add__(p2)
print(p3)
dist=p1.distance(p3)
print(dist)
del p1
print(f"Counter {Point.counter}") 

