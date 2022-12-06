with open("input.txt", "r") as f:
    list = f.read().splitlines()

s = list[0]
for i in range(len(s) - 14):
    c = [s[i], s[i + 1], s[i + 2], s[i + 3], s[i + 4], s[i + 5], s[i + 6], s[i + 7], s[i + 8], s[i + 9], s[i + 10], s[i + 11], s[i + 12], s[i + 13]]
    u = {i for i in c}
    if len(u) == 14:
        print(i + 14)
        break