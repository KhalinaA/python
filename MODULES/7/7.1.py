lst = [str(s) for s in input().split(" ")]
lst1 = []
for i in lst:
    if lst1.count(i) == 0:
        lst1.append(i)
        print(0, end=" ")
    else:
        lst1.append(i)
        print(lst1.count(i)-1, end=" ")
