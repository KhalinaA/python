n = int(input('Введите минуты прошедшие после полуночи:'))
hours = n % (60 * 24) // 60
minutes = n % 60
print(f'{hours}:{minutes}')