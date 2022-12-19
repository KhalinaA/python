s = input()
lst = [int(s) for s in s.split()]
for i in lst:
    if int(i) % 2 != 0:
        print(i, end=' ')
