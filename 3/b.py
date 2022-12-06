with open("input.txt", "r") as f:
    list = f.read().splitlines()

sum = 0
for i in range(0, len(list) // 3):
    j = i * 3
    first = {i for i in list[j]}
    second = {i for i in list[j + 1]}
    third = {i for i in list[j + 2]}
    common = first.intersection(second).intersection(third)
    common = common.pop()
    if common.islower():
        common = ord(common) - 96
    else:
        common = ord(common) - 38
    sum += common
print(sum)