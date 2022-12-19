s = input()
h1 = s.index("h", 0, len(s))
h2 = s.rindex("h", h1 + 1, len(s))
s_new = s[h1+1:h2]
s_new_rev = s_new[::-1]
s1 = s[:h1+1]
s2 = s[h2:]
print(s1, s_new_rev, s2, sep="")