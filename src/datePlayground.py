#
# datePlayground.py
# playing around with date stuff
#

import datetime

today = datetime.datetime.now()


def printDateInfo():
    print(today.date())
    print(today.isocalendar())
    print(today.weekday())


printDateInfo()

today = today + datetime.timedelta(days=1)

print(today.date())
print(today.isocalendar())
print(today.weekday())
