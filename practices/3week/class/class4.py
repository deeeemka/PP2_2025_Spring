class point():
    def __init__(self):
        pass
    def inp(self , x , y):
        self.x = x
        self.y = y
    def show(self):
        print("Your point coorsinats are: " , self.x , self.y)
    def move(self , dx , dy):
        self.x += dx
        self.y += dy
    def dist(self , x_other , y_other):
        print(((self.x - x_other)**2 + (self.y - y_other)**2)**0.5)
a = point()
x = int(input("Your x: "))
y = int(input("Your y: "))
a.inp(x , y)
a.show()
dx = int(input("Your dx: "))
dy = int(input("Your dy: "))
a.move(dx , dy)
x_other = x
y_other = y
a.dist(x_other , y_other)