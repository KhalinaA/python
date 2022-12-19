n = int(input())
d = {}
for i in range(n):
    lst = [str(s) for s in input().split(" ")]
    for j in lst:
        try:
            d[j] = d[j] + 1
        except:
            d[j] = 1
print(sorted(d.values(), reverse=True))