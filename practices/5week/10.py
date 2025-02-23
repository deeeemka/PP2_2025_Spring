import re
def reg(s):
    pattern = r'[A-Z]'
    ans = ''
    for i in range(len(s)):
        if re.match(pattern , s[i]):
            ans += " " + s[i]
        else:
            ans += s[i]
    arr = ans.split()
    pattern = r'[A-Z]'
    new_arr = []
    for word in arr:
        new_str = ''
        for i in range(len(word)):
            if re.match(pattern , word[i]):
                new_str += word[i].lower()
            else:
                new_str += word[i]
        new_arr.append(new_str)
    result = "_".join(new_arr)
    print(result)
s = str(input())
reg(s)