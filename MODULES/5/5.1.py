n = int(input('Введите число больше 2-х: '))
i = 1
while i <= n:
    i = i + 1
    if n % i == 0:
        print(i)
        break