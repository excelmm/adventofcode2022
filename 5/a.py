with open("input.txt", "r") as f:
    list = f.read().splitlines()

s1 = ['W', 'R', 'F']
s2 = ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P']
s3 = ['P', 'M', 'Z', 'N', 'L']
s4 = ['J', 'C', 'H', 'R']
s5 = ['C', 'P', 'G', 'H', 'Q', 'T', 'B']
s6 = ['G', 'C', 'W', 'L', 'F', 'Z']
s7 = ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C']
s8 = ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C']
s9 = ['J', 'W', 'H', 'G', 'R', 'S', 'V']

stacks = [[1], s1, s2, s3, s4, s5, s6, s7, s8, s9]

for i in list:
    j = i.split(' ')
    q = int(j[1])
    o = int(j[3])
    d = int(j[5])
    for _ in range(q):
        stacks[d].append(stacks[o][-1])
        stacks[o] = stacks[o][:-1]

for i in stacks:
    print(i[-1],end="")