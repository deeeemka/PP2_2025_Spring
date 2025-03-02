n = int(input())
arr = []
for i in range(n):
    a = input()
    arr.append(a)
tup = tuple(arr)
print(all(tup))