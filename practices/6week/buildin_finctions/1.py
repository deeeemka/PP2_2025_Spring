from functools import reduce
def ans(arr):
    mult = reduce(lambda x , y : x*y , arr)
    print(mult)
n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
ans(arr)