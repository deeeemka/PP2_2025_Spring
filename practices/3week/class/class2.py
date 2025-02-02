class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self,length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length**2
inp = int(input())
shape = shape()
print('defoult area: ',shape.area())
print(square(inp).area())
    