def palin(s):
    s = s.lower()
    s.replace(" ","")
    if s == s[::-1]:
        return True
a = str(input())
if palin(a):
    print("YES")
else:
    print("NO")