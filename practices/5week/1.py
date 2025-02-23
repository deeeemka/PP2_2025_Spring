import re
def reg(s):
    if re.search('ab*', s):
        return True
    else:
        return False
s = str(input())
if reg(s):
    print('yes')
else:
    print("no")