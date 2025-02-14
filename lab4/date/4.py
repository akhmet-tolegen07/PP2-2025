import datetime

x = datetime.datetime.today()

y = datetime.datetime(2013, 12, 24)

diff = x - y
print(diff.total_seconds())