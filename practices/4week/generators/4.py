a = int(input())
b = int(input())
def gen(a , b):
    for i in range(a , b+1):
        ans = i**2
        yield ans
a = gen(a , b)
for i in range(a , b+1):
    print(next(a))