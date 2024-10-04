import datetime

currunt_dt = datetime.datetime.now()

print(currunt_dt)

formeting_datetime = currunt_dt.strftime("%d-%m-%y  %H:%M:%S ")
print(formeting_datetime)