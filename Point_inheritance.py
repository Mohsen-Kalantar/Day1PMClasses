class Point(object):
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

class Point3d(Point):
    def __init__(self, vx, vy, vz):
#         super().__init__(vx,vy)
        Point.__init__(self,vx,vy)
        self.z=vz
    def __str__(self):
        return super().__str__()+f" {self.z}"
    
if __name__ == "__main__":        
    p1=Point3d(2,3,1)
    print(p1)
    
