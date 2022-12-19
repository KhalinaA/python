n = int(input('Введите номер эл-та из ряда Фибоначчи:'))
fib_1 = 1
fib_2 = 1
i = 0
while i < n-2:
   fib_sum = fib_1 + fib_2
   fib_1 = fib_2
   fib_2 = fib_sum
   i += 1
print(fib_2)

