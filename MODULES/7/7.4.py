n = int(input())
dict1 = {}
for i in range(n):
    lst = [str(s) for s in input().split(" ")]
    for j in lst:
        try:
            dict1[j] = dict1[j]+1
        except:
            dict1[j] = 1
max_dict = {k: v for k, v in dict1.items() if v == max(dict1.values())}
print(sorted(max_dict.items()))
