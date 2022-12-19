s = input()
h1 = s.index("h", 0, len(s))
h2 = s.rindex("h", h1+1, len(s))
s1 = s[:h1]
s2 = s[h2+1:]
print(s1, s2, sep="")