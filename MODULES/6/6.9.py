s = input()
len1 = len(s)
if len1 % 2 == 1:
    s1 = s[:(len1//2)+1]
    s2 = s[(len1//2)+1:]
else:
    s1 = s[:(len1 // 2)]
    s2 = s[(len1 // 2):]
print(s2, s1, sep="")