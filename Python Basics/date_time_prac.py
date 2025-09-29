import datetime


now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond) 


today = datetime.date.today()
print("Today's date:", today)
print("Weekday (0=Monday, 6=Sunday):", today.weekday())
print("ISO Weekday (1=Monday, 7=Sunday):", today.isoweekday())

custom_date = datetime.date(2023, 1, 1)
print("Custom date:", custom_date)  
delta = datetime.timedelta(days=10)
new_date = today + delta

format_date = new_date.strftime("%Y-%m-%d")
print("New date after 10 days:", format_date)
parsed_date = datetime.datetime.strptime("2023-12-25", "%Y-%m-%d")
print("Parsed date:", parsed_date)  