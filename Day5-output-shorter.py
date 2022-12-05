lines = None
with open("Day5-input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if lines[i][-1] == "\n":
        lines[i] = lines[i][:-1]

cratesLines = None
moves = None
stacks = None

def initProblem():
    global cratesLines, moves, stacks
    cratesLines = []
    moves = []
    for line in lines:
        if "[" in line: #only in crate lines
            cratesLines.append(line)
        if "move" in line: #only lines with "move x ..."
            moves.append(line)
    
    for i in range(len(moves)):
        moves[i] = list(map(int, moves[i].split(" ")[1:6:2]))
    
    cratesLines.reverse()
    stacks = []
    for i in range((len(lines[0]) +1)//4):
        stacks.append([])
    
    for line in cratesLines:
        list(map(list.append, [stacks[i] for i in range(len(stacks)) if line[i*4+1] != " "], [line[i] for i in range(1, len(stacks)*4-1, 4) if line[i] != " "]))

initProblem()

for move in moves:
    for j in range(move[0]):
        stacks[move[2]-1].append(stacks[move[1]-1].pop())

print("Star 1:", "".join([s[-1] for s in stacks]))

initProblem()

for move in moves:
    temp = []
    for j in range(move[0]):
        temp.append(stacks[move[1]-1].pop())
    stacks[move[2]-1] += temp[::-1]

print("Star 2:", "".join([s[-1] for s in stacks]))