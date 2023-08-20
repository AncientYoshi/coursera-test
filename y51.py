import sys
import os

locations = sys.path

for location in locations:
    if os.path.isdir(location):
        print(location)

        for root, dirs, files in os.walk(location):
            for file in files:
                print(os.path.join(root, file))

import calendar

leapdays = calendar.leapdays(2000, 2023)

print(leapdays)

isitleap = calendar.isleap(2077)

print(isitleap)
