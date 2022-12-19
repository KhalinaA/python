lst = [int(s) for s in input().split(" ")]
lst1 = []
for i in lst:
    if lst1.count(i) != 0:
        print ("ДА")
    else:
        print("НЕТ")
        lst1.append(i)