import re
def reg(s):
    if re.search(r'[A-Z]{1}[a-z]+', s):
        return True
    else:
        return False
s = str(input())
if reg(s):
    print('good')
else:
    print('bad')