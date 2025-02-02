def unique():
    a = int(input())
    arr=[]
    answer=[]
    for i in range(a):
        elem = int(input())
        arr.append(elem)
    for i in arr:
        if i not in answer:
            answer.append(i)
    print(answer)
unique()