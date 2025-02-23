import re
def reg(s):
    pattern = r'a.+b'
    if re.search(pattern , s):
        return True
    else:
        return False
s = str(input())
if reg(s):
    print('good')
else:
    print('bad')