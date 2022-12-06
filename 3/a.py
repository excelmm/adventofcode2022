with open("input.txt", "r") as f:
    list = f.read().splitlines()

sum = 0
for i in list:
    first, second = i[:len(i)//2], i[len(i)//2:]
    first = {i for i in first}
    second = {i for i in second}
    common = first.intersection(second)
    common = common.pop()
    if common.islower():
        common = ord(common) - 96
    else:
        common = ord(common) - 38
    sum += common
print(sum)