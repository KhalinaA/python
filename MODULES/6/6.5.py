s, t = (input() for _ in range(2))

counter = 0
for i in range(len(s)):
    if s.find(t, i, i + len(t)) >= 0:
        counter += 1
print(counter)
