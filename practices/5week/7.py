import re
def reg(s):
    pattern = r'[_]+'
    new = re.sub(pattern , ' ' , s)
    spl = list(new.split())
    new_verb = ''
    for i in spl:
        verb = i.capitalize()
        new_verb += verb

    print(new_verb[0].lower() + new_verb[1:])
s = str(input())
reg(s)