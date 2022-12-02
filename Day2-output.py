lines = None
with open("Day2-input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

plays = {"X": 1, "Y":2, "Z":3}
result = [0, 3, 6]

total = 0
for i in range(len(lines)):
    currRound = lines[i].split(" ")
    total += plays[currRound[1]]
    if currRound[0] == "A" and currRound[1] == "Y":
        total += result[2]
    if currRound[0] == "B" and currRound[1] == "Z":
        total += result[2]
    if currRound[0] == "C" and currRound[1] == "X":
        total += result[2]
    if currRound[0] == "A" and currRound[1] == "X":
        total += result[1]
    if currRound[0] == "B" and currRound[1] == "Y":
        total += result[1]
    if currRound[0] == "C" and currRound[1] == "Z":
        total += result[1]
    
print("Star 1:", total)

plays = {"X": 0, "Y":3, "Z":6}
total = 0
for i in range(len(lines)):
    currRound = lines[i].split(" ")
    total += plays[currRound[1]]
    if currRound[0] == "A" and currRound[1] == "X":
        total += 3
    if currRound[0] == "A" and currRound[1] == "Y":
        total += 1
    if currRound[0] == "A" and currRound[1] == "Z":
        total += 2
    if currRound[0] == "B" and currRound[1] == "X":
        total += 1
    if currRound[0] == "B" and currRound[1] == "Y":
        total += 2
    if currRound[0] == "B" and currRound[1] == "Z":
        total += 3
    if currRound[0] == "C" and currRound[1] == "X":
        total += 2
    if currRound[0] == "C" and currRound[1] == "Y":
        total += 3
    if currRound[0] == "C" and currRound[1] == "Z":
        total += 1

print("Star 2:", total)