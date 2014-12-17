"""
One useful class method to override is the built-in __repr__() method, which is short for representation; by providing a return
value in this method, we can tell Python how to represent an object of our class
"""

class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)

print my_point
