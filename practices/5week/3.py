import re
def reg(s):
    if re.search(r'[a-z]+_[a-z]', s):
        return True
    else:
        return False
s = str(input())
if reg(s):
    print('good')
else:
    print("bad")