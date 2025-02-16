import math
n = int(input("Input the number of sides: "))
h = int(input("Input the length of one side: "))
area = math.prod(([n , pow(h, 2)])) / math.prod([4 , math.tan(math.pi/n) ])
print("The area og the pollygon: ", round.area)
