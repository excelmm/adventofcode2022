with open("input.txt", "r") as f:
    list = f.read().splitlines()

count = 0
for k in list:
    i = k.split(",")
    l1, u1 = [int(j) for j in i[0].split('-')]
    l2, u2 = [int(j) for j in i[1].split('-')]
    if l1 <= l2 and u1 >= u2:
        count += 1
    elif l1 >= l2 and u1 <= u2:
        count += 1
print(count)