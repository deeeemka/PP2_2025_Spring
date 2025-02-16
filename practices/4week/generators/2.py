n = int(input())
def even(nums):
    for i in nums:
        if  i%2 == 0:
            yield i
squared = even(n)
a = list(squared)
a2=str(a)
ans = ",".join(a2)
print(a2)
