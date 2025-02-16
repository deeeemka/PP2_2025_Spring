import datetime
date_f = '%Y-%m-%d %H:%M:%S'
date1=input()
date2= input()
new_date1=datetime.datetime.strptime(date1 , date_f)
new_date2=datetime.datetime.strptime(date2 , date_f)
difference = new_date2 - new_date1
print(difference.total_seconds())