def gen(a):
    for i in range(a+1):
        if i%3 == 0 and i%4 == 0 and i != 0:
            yield i

n = int(input())
ans = gen(n)
for i in range(n+1):
    print(next(ans))