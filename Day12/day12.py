def toGraph(lst):
    ret = {}
    for entry in lst:
        node1 = entry.split('-')[0].strip()
        node2 = entry.split('-')[1].strip()
        if node1 not in ret and node2 != 'start':
            ret[node1] = [node2]
        elif node1 in ret and node2 != 'start':
            ret[node1].append(node2)
        if node2 not in ret and node1 != 'start':
            ret[node2] = [node1]
        elif node2 in ret and node1 != 'start':
            ret[node2].append(node1)
    
    # remove end from keys
    ret.pop('end')
    return ret

def isAllowedToVisit(lst, char, allowOnlySingleLowecase=True):
    if char not in lst:
        return True
    if allowOnlySingleLowecase: return False

    freqs = {}
    for c in lst:
        if not c.islower() or c == 'end':
            continue
        if c in freqs:
            freqs[c]+=1
        else:
            freqs[c]=1
    for c in freqs:
        if freqs[c]>1:
            return False

    return True
f = open("input.txt", "r")
connections = []
for line in f.readlines():
    connections.append(line)

connectionsGraph = toGraph(connections)

#get all paths from start to end that visit
visitedList = []

def depthFirst(graph, currentVertex, visited, allowOnlySingleLowecase=True):
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex == 'end':
            visited.append('end')
        elif vertex.islower() and not isAllowedToVisit(visited, vertex, allowOnlySingleLowecase):
            continue
        elif vertex != 'end':
            depthFirst(graph, vertex, visited[:], allowOnlySingleLowecase)
            

    if len(visited)>0 and visited[-1]=='end':
        visitedList.append(visited)

depthFirst(connectionsGraph, 'start', [], True)
print("Paths with visiting small caves once are: " + str(len(visitedList)))

visitedList = []
depthFirst(connectionsGraph, 'start', [], False)
print("Paths with visiting one small caves twice are: " + str(len(visitedList)))