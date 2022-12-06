with open("input.txt", "r") as f:
    list = f.read().splitlines()

sums = []
current = 0
for i in list:
    if i != '':
        current += int(i)
    else:
        sums.append(current)
        current = 0

sums.append(current)
sums = sorted(sums,reverse=True)
print(sum(sums[:3]))