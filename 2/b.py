with open("input.txt", "r") as f:
    list = f.read().splitlines()

list = [(x[0], x[2]) for x in list]
sum = 0
for i in list:
    if i[1] == 'X':
        sum += 0
        if i[0] == 'A':
            sum += 3
        if i[0] == 'B':
            sum += 1
        if i[0] == 'C':
            sum += 2
    if i[1] == 'Y':
        sum += 3
        if i[0] == 'A':
            sum += 1
        if i[0] == 'B':
            sum += 2
        if i[0] == 'C':
            sum += 3
    if i[1] == 'Z':
        sum += 6
        if i[0] == 'A':
            sum += 2
        if i[0] == 'B':
            sum += 3
        if i[0] == 'C':
            sum += 1
print(sum)