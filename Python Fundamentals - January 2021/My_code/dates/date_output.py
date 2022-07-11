"""
Return the year and name of weekday:
"""
import datetime

x = datetime.datetime.now()

print(x.year)  # 2022
print(x.strftime("%a"))  # Tue
print(x.strftime("%A"))  # Tuesday
print(x.strftime("%w"))  # 2
print(x.strftime("%Y"))  # 2022





