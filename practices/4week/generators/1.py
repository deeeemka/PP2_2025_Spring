n = int(input())
def square(a):
    for i in range(a +1):
        yield i**2
sq = square(n)
for i in range(n+1):
    print(next(sq))