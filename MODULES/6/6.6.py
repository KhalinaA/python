lst1 = [int(s) for s in input().split(" ")]
lst2 = [int(s) for s in input().split(" ")]
for i in lst1:
    for j in lst2:
        if i == j:
            print(i, end=" ")
            break