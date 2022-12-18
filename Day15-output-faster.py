#this isn't actually faster it seems. Only in complexity but the input is too small here.
ls = None
file = "Day15-input.txt"
with open(file) as f:
    ls = list(map(lambda l:l.strip("\n").split(), f.readlines()))

def getDist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def getDistLine(p, l):
    return abs(p[1] - l)

def getDistInLine(sensor, distance, l):
    return distance - (getDistLine(sensor, l))

def mergeRanges(ranges):
    global lineCheck
    ranges.sort()
    while len(ranges) != 1:
        if ranges[1][0] > ranges[0][1]+1:
            return ranges[0][1]+1
        ranges[0] = (ranges[0][0], max(ranges[0][1], ranges[1][1]))
        del ranges[1]
        
    if ranges[0][0] != 0:
        return 0
    if ranges[-1][1] != lineCheck:
        return lineCheck
    

beacons = set()
notBeacons = set()
lineCheck = None
if file == "Day15-inputtest.txt":
    lineCheck = 10
else:
    lineCheck = 2000000
for i in range(len(ls)):
    l = ls[i]
    break
    sensor = (int(l[2][2:-1]), int(l[3][2:-1]))
    beacon = (int(l[8][2:-1]), int(l[9][2:]))
    if beacon[1] == lineCheck:
        beacons.add(lineCheck)
    dist = abs(beacon[1]-sensor[1]) + abs(beacon[0]-sensor[0])
    if sensor[1]-dist <= lineCheck and lineCheck <= sensor[1] + dist:
        distInLine = dist - abs(sensor[1]-lineCheck)
        for i in range(-distInLine, distInLine+1):
            notBeacons.add(sensor[0] + i)
    

print("Star 1:", len(notBeacons.difference(beacons)))

sensors = set()
if file == "Day15-inputtest.txt":
    lineCheck = 20
else:
    lineCheck = 4000000
for i in range(len(ls)):
    l = ls[i]
    sensor = (int(l[2][2:-1]), int(l[3][2:-1]))
    beacon = (int(l[8][2:-1]), int(l[9][2:]))
    dist = abs(beacon[1]-sensor[1]) + abs(beacon[0]-sensor[0])
    sensors.add((sensor, dist))

left = None
stop = False
counter = 0
for l in range(0, lineCheck+1):
    counter += 1
    if counter % 10000 == 0:
        print(counter)
    if stop:
        break
    ranges = []
    for s in sensors:
        sensor = s[0]
        dist = s[1]
        
        if getDistLine(sensor, l) > dist:
            continue
        
        distIn = getDistInLine(sensor, dist, l)
        range_ = (max(0, sensor[0]-distIn), min(lineCheck, sensor[0]+distIn))
        ranges.append(range_)
    coord = mergeRanges(ranges)
    if coord == None:
        continue
    left = (coord, l)
    break

print("star 2:", 4000000*left[0] + left[1])