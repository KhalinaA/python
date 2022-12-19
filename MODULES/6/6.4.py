lst=[int(s) for s in input().split()]
indx_max = 0
indx_min = 0

for s in range(1, len(lst)):
   if lst[s] > lst[indx_max]:
      indx_max = s
   if lst[s] < lst[indx_min]:
      indx_min = s
lst[indx_max], lst[indx_min] = lst[indx_min], lst[indx_max]
print(' '.join([str(s) for s in lst]))
