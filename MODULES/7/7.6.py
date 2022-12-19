n1 = int(input())
d = {}
for i in range(n1):
    lst = [str(s) for s in input().split(" ")]
    d[lst[0]] = list(lst[1:])
n2 = int(input())
a = []
for i in range(n2):
    city = input()
    for k, v in d.items():
        if d[k].count(city) != 0:
            a.append(k)
print(a)