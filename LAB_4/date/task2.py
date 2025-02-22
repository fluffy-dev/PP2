from datetime import datetime, timedelta

now = datetime.now()
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)
print(yesterday.date())
print(now.date())
print(tomorrow.date())