ls = None
with open("Day5-input.txt") as f:
    ls = f.readlines()

for i in range(len(ls)):
    if ls[i][-1] == "\n":
        ls[i] = ls[i][:-1]

sts = None
crs = None
mvs = None

def setup():
    global sts,crs,mvs
    crs = []
    mvs = []
    for i in ls:
        if "[" in i:
            crs.append(i)
        if "move" in i:
            mvs.append(i)
    mvs = list(map(str.split, mvs))
    for i in range(len(mvs)):
        mvs[i][1] = int(mvs[i][1])
        mvs[i][3] = int(mvs[i][3])
        mvs[i][5] = int(mvs[i][5])
    crs.reverse()
    sts = []
    for i in range((len(crs[0])+1)//4):
        sts.append([])
    
    for c in crs:
        list(map(list.append, [sts[i] for i in range(len(sts)) if c[i*4+1] != " "], [c[i] for i in range(1, len(c), 4) if c[i] != " "]))

setup()
for m in mvs:
    for i in range(m[1]):
        sts[m[5]-1].append(sts[m[3]-1].pop())

print("Star 1:", "".join([sts[i][-1] for i in range(len(sts))]))

setup()
for m in mvs:
    tmp=[]
    for i in range(m[1]):
        tmp.append(sts[m[3]-1].pop())
    sts[m[5]-1]+=tmp[::-1]

print("Star 2:", "".join([sts[i][-1] for i in range(len(sts))]))