def ans(s):
    arr = []
    for i in range(len(s)):
        if s[i].isupper():
            arr.append(1)
    answer = sum(arr)
    print(answer)
s = str(input())
ans(s)