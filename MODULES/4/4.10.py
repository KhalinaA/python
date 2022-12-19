x = int(input())
y = int(input())
if x % 2 == 0:
   if y % 2 != 0:
      print('Белые')
   else:
      print('Черные')
else:
   if y % 2 != 0:
      print('Черные')
   else:
      print('Белые')
