#month = input("what month of the year are you interested in?")
#print(month)


#import monthtime

#x = monthtime.monthtime.year()
#print(x.month)
#print(x.monthtime("a"))


import datetime

user_time = int(input("Enter a month (as a number): "))
user_day = int(input("Enter a day (as a number): "))
if 1 <= user_time <= 12:
    user_datetime = datetime.datetime(2023, user_time, user_day)
    month_name = user_datetime.strftime("%B")
    day_name = user_datetime.strftime("%A")
    print(f"The month for {user_time}: {month_name}, {day_name}")
else:
    print("Invalid month numbers")
   