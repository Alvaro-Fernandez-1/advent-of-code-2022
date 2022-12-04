lines = None
with open("Day4-inputtest.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if lines[i][-1] == "\n":
        lines[i] = lines[i][:-1]

value = 0
for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    elf1 = lines[i][0]
    elf2 = lines[i][1]
    elf1 = elf1.split("-")
    elf2 = elf2.split("-")
    if int(int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])):
        value += 1
    elif int(int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])):
        value += 1

print("Star 1:", value)

value = 0
for i in range(len(lines)):
    elf1 = lines[i][0]
    elf2 = lines[i][1]
    elf1 = elf1.split("-")
    elf2 = elf2.split("-")
    if int(int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1])):
        value += 1
    elif int(int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[0])):
        value += 1  

print("star 2:", value)