import datetime
import calendar

day = 13
month = 12 
year = 2019

def week_day(d, m, y):
    return calendar.day_name[datetime.datetime(y, m, d).weekday()] 

print(week_day(day, month, year))