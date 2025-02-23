import re
def reg(s):
    pattern = r'^[a-zA-Z]+$'
    if re.search(pattern , s):
        return True
    else:
        return False
s = str(input())
a = ''
if reg(s):
    a = ' '.join(s.upper())
    print(a)
else:
    print('no')