a = int(input('Введите целые неотрицательные числа (закончить нулем):\n'))
max_1 = 0
max_2 = 0
while a != 0:
   b = int(input())
   if a == b:
      max_1 += 1
      if max_1 > max_2:
         max_2 = max_1
   else:
      max_1 = 0
   a = b
print(max_2 + 1)