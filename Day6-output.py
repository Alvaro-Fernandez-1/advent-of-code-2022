ls = None
with open("Day6-inputtest.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

l, = ls
v = 0
for i in range(len(l)):
    if len(set(l[i:i+4]))==4:
        v=i+4
        break

print("Star 1:", v)

v = 0
for i in range(len(l)):
    if len(set(l[i:i+14]))==14:
        v=i+14
        break

print("star 2:", v)