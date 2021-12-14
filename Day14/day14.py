def getMinMaxDifference(m):
    minF = float('inf')
    maxF = 0
    for key in m:
        minF = min(m[key], minF)
        maxF = max(m[key], maxF)
    
    return int(maxF)-int(minF)

def getNextState(prevState, keyMap):
    ret = {}
    for state in prevState:
        char = keyMap[state]
        first = state[0] + char
        second = char + state[1]
        if first not in ret:
            ret[first] = prevState[state]
        else:
            ret[first] += prevState[state]
        if second not in ret:
            ret[second] = prevState[state]
        else:
            ret[second] += prevState[state]
    return ret

def updateCharQuantityMap(pair_frequencies, firstChar):
    ret = {}
    for pair in pair_frequencies:
        if pair[1] not in ret:
            ret[pair[1]] = pair_frequencies[pair]
        else:
            ret[pair[1]] += pair_frequencies[pair]
    
    ret[firstChar] += 1
    return ret

f = open("input.txt", "r")
template = ""
rules = {}
firstElement=True
for line in f.readlines():
    if firstElement:
        template = line.strip()
        firstElement=False
    elif line[0]!='\n':
        line = line.split(' -> ')
        rules[line[0]]=line[1].strip()

steps = 40
stepOutput = template
print("Template: " + template)
pair_frequencies = {}
char_frequencies = {}
firstElement = template[0]

# Getting initial pair frequencies
for i in range(1, len(template)):
    pair = template[i-1]+template[i]
    if pair not in pair_frequencies:
        pair_frequencies[pair] = 1
    else:
        pair_frequencies[pair] += 1

# Now caclulating sums
for i in range(steps):
    pair_frequencies = getNextState(pair_frequencies, rules)
    char_frequencies = updateCharQuantityMap(pair_frequencies, firstElement)
    print("Step: "+str(i+1)+" | Max difference: " + str(getMinMaxDifference(char_frequencies)))