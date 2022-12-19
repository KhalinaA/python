numbers = {}
def check_number(number):
   if (number[0] == '+') and (number[1] == "7") and (len(number) == 12):
      return number
   elif (number[0] == '8') and (len(number) == 11):
      check_number = '+7' + number[1:]
      return check_number
   elif (len(number) == 10):
      check_number = '+7' + number
      return check_number
   else:
      print(number)
      return False
print("  Вам доступены команды: добавить, поменять, удалить, показать контакты, закончить")
while True:
   move = str(input('Что вы хотите сделать?'))
   if (move == "добавить"):
      name = str(input('Введите имя:')).title()
      number = str(input('Введитое номер:'))
      if check_number(number):
            number = check_number(number)
            numbers[name] = number
      else:
            print('Неправильный номер')
   elif (move =="поменять"):
      name = str(input('Введите имя:')).title()
      number = str(input('Введитое номер:'))
      if check_number(number):
         number = check_number(number)
         numbers[name] = number
      else:
            print('Неправильный номер')
   elif (move == "удалить"):
      name = str(input()).title()
      if (name in numbers.keys()):
         del numbers[name]
   elif (move == "показать контакты"):
      print(numbers)
   elif (move == 'закончить'):
      break
