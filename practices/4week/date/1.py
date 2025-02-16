import datetime
x = datetime.datetime.now()
y = datetime.timedelta(days=5)
x -=y
print(x)