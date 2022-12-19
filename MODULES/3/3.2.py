s = str(input('Введите два слова:'))
print(s[s.find(' ')+1:]+' '+s[:s.find(' ')+1])
