import copy

ls = None
with open("Day19-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

def I(list_):
    for i in range(len(list_)):
        list_[i] = int(list_[i])
    return list_


blueprints = []
for i in range(len(ls)):
    l = ls[i].split()
    l = I([l[6], l[12], l[18], l[21], l[27], l[30]])
    blueprint = {"ore": l[0],
                 "clay": l[1],
                 "obsidian": (l[2], l[3]),
                 "geode": (l[4], l[5])}
    blueprints.append(blueprint)

def update(state):
    state["geode"] += state["geodeR"]["quantity"]
    state["obsidian"] += state["obsidianR"]["quantity"]
    state["clay"] += state["clayR"]["quantity"]
    state["ore"] += state["oreR"]["quantity"]
    state["time"] += 1

def getUpperBound(state, time):
    currentTime = state["time"]
    ore = state["ore"]
    obsidian = state["obsidian"]
    oreR = state["oreR"]["quantity"]
    obsidianR = state["obsidianR"]["quantity"]
    
    geode = state["geode"]
    geodeR = state["geodeR"]["quantity"]
    geodeROre = state["geodeR"]["price"]["ore"]
    geodeRObsidian = state["geodeR"]["price"]["obsidian"]
    while currentTime < time + 1:
        geode += geodeR
        if geodeROre <= ore and geodeRObsidian <= obsidian:
            ore -= geodeROre
            obsidian -= geodeRObsidian
            geodeR += 1
        ore += oreR
        obsidian += obsidianR
        oreR += 1
        obsidianR += 1
        currentTime += 1
    return geode

counter = 1
where = [0] * 33
def solve(state, best, time):
    global counter
    counter += 1
    if state["time"] == time+1:
        return max(best, state["geode"])
    if best >= getUpperBound(state, time):
        return best
    
    canBuy = []
    maxOre = max(state["geodeR"]["price"]["ore"],
                 state["obsidianR"]["price"]["ore"],
                 state["clayR"]["price"]["ore"])
    
    if state["geodeR"]["price"]["ore"] <= state["ore"] and \
       state["geodeR"]["price"]["obsidian"] <= state["obsidian"]:
        newState = copy.deepcopy(state)
        update(newState)
        newState["geodeR"]["quantity"] += 1
        newState["obsidian"] -= state["geodeR"]["price"]["obsidian"]
        newState["ore"] -= state["geodeR"]["price"]["ore"]
        canBuy.append(1)
        newState["debug"].append("geode")
        where[state["time"]] = 0
        best = max(best, solve(newState, best, time))
        if counter%10000 == 0:
            print(best, state["time"], "geode")
            print(where)
    if state["obsidianR"]["price"]["ore"] <= state["ore"] and \
       state["obsidianR"]["price"]["clay"] <= state["clay"]:
        newState = copy.deepcopy(state)
        update(newState)
        newState["obsidianR"]["quantity"] += 1
        newState["clay"] -= state["obsidianR"]["price"]["clay"]
        newState["ore"] -= state["obsidianR"]["price"]["ore"]
        canBuy.append(1)
        newState["debug"].append("obsidian")
        where[state["time"]] = 1
        best = max(best, solve(newState, best, time))
        if counter%10000 == 0:
            print(best, state["time"], "obsidian")
            print(where)
    if state["clayR"]["price"]["ore"] <= state["ore"]:
        newState = copy.deepcopy(state)
        update(newState)
        newState["clayR"]["quantity"] += 1
        newState["ore"] -= state["clayR"]["price"]["ore"]
        canBuy.append(1)
        newState["debug"].append("clay")
        where[state["time"]] = 2
        best = max(best, solve(newState, best, time))
        if counter%10000 == 0:
            print(best, state["time"], "clay")
            print(where)
    if state["oreR"]["price"]["ore"] <= state["ore"] and \
       state["oreR"]["quantity"] < maxOre:
        newState = copy.deepcopy(state)
        update(newState)
        newState["oreR"]["quantity"] += 1
        newState["ore"] -= state["oreR"]["price"]["ore"]
        canBuy.append(1)
        newState["debug"].append("ore")
        where[state["time"]] = 3
        best = max(best, solve(newState, best, time))
        if counter%10000 == 0:
            print(best, state["time"], "ore")
            print(where)
            
    if len(canBuy) == 4:
        return best
    
    newState = copy.deepcopy(state)
    newState["debug"].append("none")
    update(newState)
    where[state["time"]] = 4
    best = max(best, solve(newState, best, time))
    if counter%10000 == 0:
        print(best, state["time"], "none")
        print(where)
    
    return best
        
    
total = 0
for b in range(len(blueprints)):
    blueprint = blueprints[b]
    state = {"time": 1,
             "ore": 0,
             "clay": 0,
             "obsidian": 0,
             "geode": 0,
             "oreR": {
                 "quantity": 1,
                 "price": {
                     "ore": blueprint["ore"]
                     }
                 },
             "clayR": {
                 "quantity": 0,
                 "price": {
                     "ore": blueprint["clay"]
                     }
                 },
             "obsidianR": {
                 "quantity": 0,
                 "price": {
                     "ore": blueprint["obsidian"][0],
                     "clay": blueprint["obsidian"][1]
                     }
                 },
             "geodeR": {
                 "quantity": 0,
                 "price": {
                     "ore": blueprint["geode"][0],
                     "obsidian": blueprint["geode"][1]
                     }
                 },
             "debug": []
             }
    solution = 0#solve(state, 0, 24)
    print("SOLVED", b+1, solution, total)
    total += (b+1) * solution
    
print("Star 1:", total)

total = 1
for b in range(min(3, len(blueprints))):
    blueprint = blueprints[b]
    state = {"time": 1,
             "ore": 0,
             "clay": 0,
             "obsidian": 0,
             "geode": 0,
             "oreR": {
                 "quantity": 1,
                 "price": {
                     "ore": blueprint["ore"]
                     }
                 },
             "clayR": {
                 "quantity": 0,
                 "price": {
                     "ore": blueprint["clay"]
                     }
                 },
             "obsidianR": {
                 "quantity": 0,
                 "price": {
                     "ore": blueprint["obsidian"][0],
                     "clay": blueprint["obsidian"][1]
                     }
                 },
             "geodeR": {
                 "quantity": 0,
                 "price": {
                     "ore": blueprint["geode"][0],
                     "obsidian": blueprint["geode"][1]
                     }
                 },
             "debug": []
             }
    solution = solve(state, 0, 32)
    print("SOLVED", b+1, solution, total)
    total *= solution

print("star 2:", total)