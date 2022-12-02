lines = None
with open("Day1-input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]


elves = [0]
currentElf = 0
for line in lines:
    if line == "":
        currentElf += 1
        elves.append(0)
        continue
    elves[currentElf] += int(line)

print("Star 1:", max(elves))

elves.sort()
print("Star 2:", elves[-3] + elves[-2] + elves[-1])
