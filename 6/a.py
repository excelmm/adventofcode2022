with open("input.txt", "r") as f:
    list = f.read().splitlines()

s = list[0]
for i in range(len(s) - 4):
    c = [s[i], s[i + 1], s[i + 2], s[i + 3]]
    u = {i for i in c}
    if len(u) == 4:
        print(i + 4)
        break