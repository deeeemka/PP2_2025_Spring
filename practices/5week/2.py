import re
def reg(s):
    if re.search('a{1}b{2,3}', s):
        return True
    else:
        return False
s = str(input())
if reg(s):
    print('good')
else:
    print("bad")