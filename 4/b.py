with open("input.txt", "r") as f:
    list = f.read().splitlines()

count = len(list)
for k in list:
    i = k.split(",")
    l1, u1 = [int(j) for j in i[0].split('-')]
    l2, u2 = [int(j) for j in i[1].split('-')]
    if u1 < l2 or u2 < l1:
        count -= 1
print(count)