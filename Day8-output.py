ls = None
with open("Day8-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

vis = []
for i in range(len(ls)):
    vis.append([])
    for j in range(len(ls[0])):
        vis[i].append([False, {"up":0, "down":0, "left":0, "right":0}])

for i in range(len(ls[0])):
    vis[0][i][0] = True
    vis[0][i][1]["up"] = ls[0][i]
    vis[-1][i][0] = True
    vis[-1][i][1]["down"] = ls[-1][i]

for i in range(len(ls)):
    vis[i][0][0] = True
    vis[i][0][1]["left"] = ls[i][0]
    vis[i][-1][0] = True
    vis[i][-1][1]["right"] = ls[i][-1]

v = 0

for i in range(1, len(ls)):
    l = ls[i]
    for j in range(len(l)):
        if l[j] > vis[i-1][j][1]["up"]:
            vis[i][j][0] = True
            vis[i][j][1]["up"] = ls[i][j]
        else:
            vis[i][j][1]["up"] = vis[i-1][j][1]["up"]

for i in range(len(ls)-2, -1, -1):
    l = ls[i]
    for j in range(len(l)):
        if l[j] > vis[i+1][j][1]["down"]:
            vis[i][j][0] = True
            vis[i][j][1]["down"] = ls[i][j]
        else:
            vis[i][j][1]["down"] = vis[i+1][j][1]["down"]

for i in range(len(ls)):
    l = ls[i]
    for j in range(1, len(l)):
        if l[j] > vis[i][j-1][1]["left"]:
            vis[i][j][0] = True
            vis[i][j][1]["left"] = ls[i][j]
        else:
            vis[i][j][1]["left"] = vis[i][j-1][1]["left"]

for i in range(len(ls)):
    l = ls[i]
    for j in range(len(l)-2, -1, -1):
        if l[j] > vis[i][j+1][1]["right"]:
            vis[i][j][0] = True
            vis[i][j][1]["right"] = ls[i][j]
        else:
            vis[i][j][1]["right"] = vis[i][j+1][1]["right"]

v=0
for i in vis:
    for j in i:
        if j[0]:
            v += 1    
print("Star 1:", v)

def score(treey, treex):
    tree = ls[treey][treex]
    up=0
    down=0
    left=0
    right=0
    for i in range(treey-1, -1, -1):
        if tree > ls[i][treex]:
            up += 1
        else:
            up += 1
            break
    
    for i in range(treey+1, len(ls)):
        if tree > ls[i][treex]:
            down += 1
        else:
            down += 1
            break
    
    for i in range(treex-1, -1, -1):
        if tree > ls[treey][i]:
            left += 1
        else:
            left += 1
            break
    
    for i in range(treex+1, len(ls[0])):
        if tree > ls[treey][i]:
            right += 1
        else:
            right += 1
            break
    
    
    return up*down*left*right
    
        

v=0
for i in range(len(ls)):
    for j in range(len(ls[i])):
        v = max(v, score(i, j))

print("star 2:", v)