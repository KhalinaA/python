n = int(input())
dict1 = {}
for i in range(n):
    lst = [str(s) for s in input().split(" ")]
    try:
        dict1[lst[0]] = int(dict1[lst[0]]) + int(lst[1])
    except:
        dict1[lst[0]] = int(lst[1])
    print(dict1)