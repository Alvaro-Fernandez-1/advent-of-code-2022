lines = None
with open("Day5-input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if lines[i][-1] == "\n":
        lines[i] = lines[i][:-1]

cratesLines = None
moves = None
stacks = None

def numStacks():
    #line 0 is a crate line for sure
    #each stack will have "[X] " and a space except the last one "[X]"
    return (len(lines[0]) +1)//4

def parseMoves():
    global moves
    for i in range(len(moves)):
        moves[i] = moves[i].split(" ")
        moves[i] = [int(moves[i][1]), int(moves[i][3]), int(moves[i][5])]

def parseCrates():
    global cratesLines
    parsed = None
    cratesLineLen = len(cratesLines[0])
    for i in range(len(cratesLines)):
        parsed = []
        for crateIndex in range(1, cratesLineLen, 4):
            parsed.append(cratesLines[i][crateIndex])
            
        cratesLines[i] = parsed

def initStacks():
    global cratesLines, stacks
    for line in cratesLines:
        for i in range(len(stacks)):
            crate = line[i]
            if crate != " ":
                stacks[i].append(crate)

#sets moves to int lists with length 3 storing each number
#sets stacks to a list of length the amount of stacks, each element a stack
#each stack is a list of characters, top of the stack is the last element
def initProblem():
    global cratesLines, moves, stacks
    cratesLines = []
    moves = []
    for line in lines:
        if "[" in line: #only in crate lines
            cratesLines.append(line)
        if "move" in line: #only lines with "move x ..."
            moves.append(line)
    
    parseMoves()
    parseCrates()
    
    cratesLines.reverse()
    stacks = []
    for i in range(numStacks()):
        stacks.append([])
    initStacks()

def lastCrates():
    result = ""
    for stack in stacks:
        result += stack[-1]
    return result

#part 1 start
initProblem()

for move in moves:
    for j in range(move[0]):
        stacks[move[2]-1].append(stacks[move[1]-1].pop())

print("Star 1:", lastCrates())

initProblem()

for move in moves:
    temp = []
    for j in range(move[0]):
        temp.append(stacks[move[1]-1].pop())
    temp.reverse()
    stacks[move[2]-1] += temp

print("Star 2:", lastCrates())