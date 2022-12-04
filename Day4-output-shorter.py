lines = None
with open("Day4-input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if lines[i][-1] == "\n":
        lines[i] = lines[i][:-1]

def ints(list_):
    for i in range(len(list_)):
        list_[i] = int(list_[i])
    return list_

v1 = v2 = 0
for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    elf1 = ints(lines[i][0].split("-"))
    elf2 = ints(lines[i][1].split("-"))
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1] or \
        elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        v1 += 1
    if elf1[0] >= elf2[0] and elf1[0] <= elf2[1] or \
        elf1[0] <= elf2[0] and elf1[1] >= elf2[0]:
        v2 += 1  

print("Star 1:", v1)
print("star 2:", v2)