c = int(input())
d = {}

for i in range(0, c):
    value_array = input().split()
    value = value_array[0]
    key = value_array[1]
    d.__setitem__(key, value)

word = str(input())
print(d[word])
