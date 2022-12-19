import datetime
m = int(input('Введите месяц:'))
d = int(input('Введите день:'))
if (m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12):
   days = 31
elif (m == 2):
   days = 28
else:
   days = 30
day = d + 1
if (day > days):
   month = m + 1
   day = 1
else:
   month = m
if (month > 12):
   year = 2023
   month = 1
else:
   year = 2022
print(f'{day}-{month}-{year}')
