import math
a = int(input('Кол-во учеников в А классе:'))
b = int(input('Кол-во учеников в Б классе:'))
c = int(input('Кол-во учеников в В классе:'))
a1 = math.ceil(a/2)
b1 = math.ceil(b/2)
c1 = math.ceil(c/2)
print(a1+b1+c1)