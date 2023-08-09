class Circle():

    pi = 3.14

    def __init__(self,radius=1): 
        self.radius= radius

    def area(self):
        return self.radius*self.radius*Circle.pi
    
    def set_radius(self,new_radius):
        self.radius= new_radius

    def get_radius(self,new_radius):
        return self.radius
    
c1 = Circle()
c1.set_radius(4)
area = c1.area()
print(f"c1 has radius {c1.get_radius()} and area {area}")    
