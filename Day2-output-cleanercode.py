lines = None
with open("Day2-input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

#r=0, p=1, s=2, but also loss=0, draw=1, win=2
plays = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}

def rockPaperScissors(p1, p2):
    if p1 == p2:
        return 1
    if p2 == (p1+1) % 3:
        return 2
    return 0

total = 0
for line in lines:
    currRound = line.split(" ")
    p1Play = plays[currRound[0]]
    p2Play = plays[currRound[1]]
    result = rockPaperScissors(p1Play, p2Play)
    total += 3*result + p2Play+1

print("Star 1:", total)

def reverseRockPaperScissors(p1, result):
    #return p2's play given p1's play and win/loss/draw
    resultAdd = [-1, 0, 1] #add to p1 to get loss, draw, win
    return (p1 + resultAdd[result]) % 3

total = 0
for line in lines:
    currRound = line.split(" ")
    p1Play = plays[currRound[0]]
    result = plays[currRound[1]]
    p2Play = reverseRockPaperScissors(p1Play, result)
    total += 3*result + p2Play+1

print("Star 2:", total)