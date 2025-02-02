class shape:
    def __init__(self):
        pass
class Rectangle(shape):
    def __init__(self,length,width):
        super().__init__()
        self.lenth = length
        self.width = width
    def area(self):
        return self.lenth * self.width
    
l = int(input("input length "))
w = int(input("input width "))
print("area ot the rectangle =", Rectangle(l,w).area())

