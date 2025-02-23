import re
def reg(s):
    pattern = r'[ ,.]+'
    print(re.sub(pattern , ':' , s))
s = str(input())
reg(s)