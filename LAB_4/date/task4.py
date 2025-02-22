from datetime import date,timedelta,datetime

a = datetime.now()-timedelta(1)
b = datetime.now()+timedelta(1)

a = datetime.timestamp(a)

b = datetime.timestamp(b)
print(b-a)