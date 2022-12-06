with open("input.txt", "r") as f:
    list = f.read().splitlines()

maxi = 0
current = 0
for i in list:
    if i != '':
        current += int(i)
    else:
        maxi = max(maxi, current)
        current = 0

maxi = max(maxi, current)
print(maxi)