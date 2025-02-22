from datetime import datetime, timedelta

now = datetime.now()
a = now.replace(microsecond=0)
print(a)
