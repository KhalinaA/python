a = int(input('Введите целые неотрицательные числа (закончить нулем):\n'))
i = 0
while a != 0:
   b = int(input())
   if b != 0 and a < b:
      i += 1
   a = b
print(i)
