import datetime

currunt_dt = datetime.datetime.now()

print(currunt_dt)

formeting_datetime = currunt_dt.strftime("%d-%m-%y  %H:%M:%S ")
print(formeting_datetime)


date1 = datetime.timedelta(2024,1,4)
date2 = datetime.timedelta(2023,4,6)

defarence = date1 - date2
print(defarence)