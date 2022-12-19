x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
a = 0
b = 0
if x % 2 == 0:
   if y % 2 != 0:
      a = 1
      
   else:
      a = 0
      
else:
   if y % 2 != 0:
      a = 0
      
   else:
      a = 1
      


if x1 % 2 == 0:
   if y1 % 2 != 0:
      b = 1
      
   else:
      b = 0
      
else:
   if y1 % 2 != 0:
      b = 0
      
   else:
      b = 1
      

if a == b:
   print('да')
else:
   print('нет')