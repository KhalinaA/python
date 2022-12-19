lst=[int(s) for s in input().split()]

for s in range(1, len(lst), 2):
   lst[s - 1], lst[s] = lst [s], lst [s - 1]

print(' '.join([str(s) for s in lst]))
