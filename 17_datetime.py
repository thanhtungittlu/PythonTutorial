import datetime

x = datetime.datetime.now()
print(x)
print(x.year) # In ra year
print(x.strftime("%A")) # In ra day


newDay = datetime.datetime(2020, 5, 17)
print(newDay)