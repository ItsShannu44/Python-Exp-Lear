# from datetime import datetime, date, time, timedelta
# # from datetime import date, time, datetime

# print(f"The current date and time is {datetime.now()}")

# print(f"future date after 7 days is {datetime.now()+timedelta(days=7)}")

# print( f'FUture date after "5" days and "10" hours is {datetime.now()+ timedelta(days=5,hours=10)}')
# print(f"The Current date and time is{datetime.now().strftime('%Y-%m-%d:%H-%M-%S')}")

# c_d=date.today()
# c_t=time(hour=10,minute=45,second=7)
# print(f"Combined date and time is: {datetime.combine(c_d,c_t)}")    




from datetime import datetime, timedelta, time, date

print(f"Current date is:{datetime.now()}")
print(f'Date after "7" days and "2" hours is: {datetime.now()+timedelta(days=7, hours=2)}')

c_d=date.today()
print("Today is:",c_d)
c_t=time()
print(f"Combining the date and time of today: {datetime.combine(c_d,c_t)}")
print(f'Current date and time is{datetime.now().strftime('%d-%m-%y : %h-%m-%S')}')

