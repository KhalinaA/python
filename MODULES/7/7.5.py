n1 = int(input())
d = {}
for i in range(n1):
    lst = [str(s) for s in input().split(" ")]
    d[lst[0]] = list(lst[1:])
n2 = int(input())
for i in range(n2):
    lst1 = [str(s) for s in input().split(" ")]
    testlst = d[lst1[1]]
    if testlst.count("R") != 0:
        testlst.remove("R")
        testlst.append("read")
    if testlst.count("W") != 0:
        testlst.remove("W")
        testlst.append("write")
    if testlst.count("X") != 0:
        testlst.remove("X")
        testlst.append("execute")
    if testlst.count(lst1[0]) != 0:
        print("OK")
    else:
        print("Denied")