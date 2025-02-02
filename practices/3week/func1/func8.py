def spy_game(nums):
    found_0 = False
    found_00 = False
    found_000 = False

    for num in nums:
        if num == 0:
            found_0 = True
        elif num == 0 and found_0:
            found_00 = True
        elif num == 7 and found_0 and found_00:
            found_000 = True
            break
    return found_0 and found_00
n = int(input())
arr=[]
for i in range(n):
    elem = int(input())
    arr.append(elem)
if spy_game(arr):
    print("True")
else:
    print('False')