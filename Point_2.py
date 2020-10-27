class Point:
    def __init__(self, vx, vy):
        self.x=vx   # attribute x is defined here
        self.y=vy   # attribute y is defined here
    def __str__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def distance(self, other):
        import math
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    def clear(self):
        self.x=self.y=0
    def __setattr__(self, name, value):
        if name not in ["x", "y"]:
            raise NameError(f"Invalid attribute name {name}") 
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid attribute value {value}")
        self.__dict__[name]=value
    def __delattr__(self, name):
        raise NameError(f"Cannot delete the attribute {name}") 
        
        
p1=Point(0,0)
print(p1.__dict__)
# 1) p1=Point.__new__()
# 2) p1.__init__(0,0) -> __init__(p1,0,0)
p2=Point(2,3)
print(p1) # <0,0>
# print(str(p1)) -> print(p1.__str__())
print(p2) # <2,3>

# p1.x="abc"
# # p1.__setattr__("x","abc")
# p1.X=12
# p1.__setattr__("X",12)
del p1.x
# p1.__delattr__("x")

print(p1) # <5,0>
# p3=p1+p2
# # p3=p1.__add__(p2)
# print(p3)
# dist=p1.distance(p3)
# print(dist)

