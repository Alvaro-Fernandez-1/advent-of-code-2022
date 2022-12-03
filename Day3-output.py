lines = None
with open("Day3-input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

value = 0

letters = "abcdefghijklmnopqrstuvwxyz"
letters += letters.upper()

for line in lines:
    a = set()
    b = set()
    for i in range(len(line)//2):
        a.add(line[i])
        b.add(line[i + len(line)//2])
    
    (common, ) = a.intersection(b)
    value += letters.find(common)+1

print("Star 1:", value)

value = 0
for i in range(len(lines)//3):
    a = set()
    b = set()
    c = set()
    
    for j in (lines[3*i]):
        a.add(j)
    for j in (lines[3*i+1]):
        b.add(j)
    for j in (lines[3*i+2]):
        c.add(j)
              
    (common,) = a.intersection(b.intersection(c))
    #print(common)
    value += letters.find(common)+1

print("star 2:", value)