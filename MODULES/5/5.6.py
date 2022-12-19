n = int(input('Введите число:\n'))
fib_1 = 1
fib_2 = 1
fib_sum  = 2
a = 1
result = -1
while fib_1 <= n:
   fib_sum = fib_1 + fib_2
   fib_1 = fib_2
   fib_2 = fib_sum
   a += 1
   if fib_1 == n:
      result = a
print(result)