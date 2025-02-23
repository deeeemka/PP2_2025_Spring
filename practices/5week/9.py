import re
def reg(s):
    pattern = r'[A-Z]'
    t =""
    for i in range(len(s)):
        if re.match(pattern , s[i]):
            t += " " + s[i]
        else:
            t += s[i]
    print(t)
s = str(input())
reg(s)