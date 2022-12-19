x = int(input('Введите число:'))
n = 0
e = 1
while e*2 <= x:
   n+=1
   e = 2**n
print(n, e)