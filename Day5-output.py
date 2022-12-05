#This one doesn't work with inputtest because the print statements
#are specifically for 9 stacks
ls = None
with open("Day5-input.txt") as f:
    ls = f.readlines()

for i in range(len(ls)):
    if ls[i][-1] == "\n":
        ls[i] = ls[i][:-1]

ls.remove("")
crs = []
for i in range(len(ls)):
    if ls[i][1]=="1":
        break
    crs.append(ls[i])

mvs = []
for i in range(len(ls)):
    if ls[i][0]!="m":
        continue
    mvs.append(ls[i])

st = []
for i in range((len(ls[0]) +1)//4):
    st.append([])
    
crs=crs[::-1]
for i in crs:
    for j in range(len(st)):
        if i[1+4*j] != " ":
            st[j].append(i[1+4*j])

for i in range(len(mvs)):
    mvs[i] = mvs[i].split(" ")
for i in mvs:
    for j in range(int(i[1])):
        st[int(i[5])-1].append(st[int(i[3])-1].pop())



print("Star 1:", st[0][-1]+st[1][-1]+st[2][-1]+
      st[3][-1]+st[4][-1]+st[5][-1]+
      st[6][-1]+st[7][-1]+st[8][-1])

crs = []
for i in range(len(ls)):
    if ls[i][1]=="1":
        break
    crs.append(ls[i])

mvs = []
for i in range(len(ls)):
    if ls[i][0]!="m":
        continue
    mvs.append(ls[i])

st = []
for i in range((len(ls[0]) +1)//4):
    st.append([])
    
crs=crs[::-1]
for i in crs:
    for j in range(len(st)):
        if i[1+4*j] != " ":
            st[j].append(i[1+4*j])

for i in range(len(mvs)):
    mvs[i] = mvs[i].split(" ")
for i in mvs:
    temp = []
    for j in range(int(i[1])):
        temp.append(st[int(i[3])-1].pop())
    temp = temp[::-1]
    for j in temp:
        st[int(i[5])-1].append(j)


print("Star 2:", st[0][-1]+st[1][-1]+st[2][-1]+
      st[3][-1]+st[4][-1]+st[5][-1]+
      st[6][-1]+st[7][-1]+st[8][-1])