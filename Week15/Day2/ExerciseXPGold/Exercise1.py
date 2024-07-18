import datetime as dt

print(dt.date.today())

holiday_name = "Christmas"
holiday_date = dt.datetime(2024, 12, 25)
current_date = dt.datetime.now()

print(f"time left until {holiday_name} : {holiday_date - current_date}")