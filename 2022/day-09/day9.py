def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def lstToCommands(lst):
    res = []
    for line in lst:
        split = line.split(' ')
        res.append([split[0], int(split[1])])
    return res

def isAdjacent(h, t):
    if (abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1) : 
        return False
    return True

def getNewIndex(command, h, t, visited):
    if command[0] == "R":
        for i in range(command[1]):
            h = [ h[0], h[1] + 1 ]
            if not isAdjacent(h, t):
                t = moveT(h, t) #[ h[0], h[1] - 1 ]
                visited.add((t[0], t[1]))
    elif command[0] == "L":
        for i in range(command[1]):
            h = [ h[0], h[1] - 1 ]
            if not isAdjacent(h, t):
                t = moveT(h, t) #[ h[0], h[1] + 1 ]
                visited.add((t[0], t[1]))
    elif command[0] == "U":
        for i in range(command[1]):
            h = [ h[0] - 1, h[1] ]
            if not isAdjacent(h, t):
                t = moveT(h, t) #[ h[0] + 1, h[1] ]
                visited.add((t[0], t[1]))
    else:
        for i in range(command[1]):
            h = [ h[0] + 1, h[1] ]
            if not isAdjacent(h, t):
                t = moveT(h, t) #[ h[0] - 1, h[1] ]
                visited.add((t[0], t[1]))
    return h, t

# top -> i-1, j
# left -> i, j-1
# bottom -> i+1, j
# right -> i, j+1

# top-right -> i-1, j+1
# top-left -> i-1, j-1
# bottom-left -> i+1, j-1
# bottom-right -> i+1, j+1
def moveT(h, t):
    if isAdjacent(h, t):
        return t
    
    y, x = t[0], t[1]
    if h[0] < t[0]:
        y = t[0] - 1
    elif h[0] > t[0]:
        y = t[0] + 1
    
    if h[1] < t[1]:
        x = t[1] - 1
    elif h[1] > t[1]:
        x = t[1] + 1
    
    return [y, x]

def moveLongTail(t_list, visited):
    for i in range(1, len(t_list)):
        t_list[i] = moveT(t_list[i-1], t_list[i])
    visited.add((t_list[-1][0], t_list[-1][1]))
    return t_list

def getNewIndexVariableTail(command, h, t, visited):
    if command[0] == "R":
        for i in range(command[1]):
            h = [ h[0], h[1] + 1 ]
            if not isAdjacent(h, t[0]):
                t[0] = moveT(h, t[0])
                t = moveLongTail(t, visited)
    elif command[0] == "L":
        for i in range(command[1]):
            h = [ h[0], h[1] - 1 ]
            if not isAdjacent(h, t[0]):
                t[0] = moveT(h, t[0]) 
                t = moveLongTail(t, visited)
    elif command[0] == "U":
        for i in range(command[1]):
            h = [ h[0] - 1, h[1] ]
            if not isAdjacent(h, t[0]):
                t[0] = moveT(h, t[0]) 
                t = moveLongTail(t, visited)
    else:
        for i in range(command[1]):
            h = [ h[0] + 1, h[1] ]
            if not isAdjacent(h, t[0]):
                t[0] = moveT(h, t[0]) 
                t = moveLongTail(t, visited)
    return h, t

def print_matrix(h, t):
    matrix = [['.' for _ in range(26)] for _ in range(21)]
    for i in range(len(t)-1, -1, -1):
        matrix[t[i][0]][t[i][1]] = str(i+1)
    matrix[h[0]][h[1]] = 'H'
    print(t[-1])
    for row in matrix:
        print(row)
    print('-------------------------------')


def part1(input):
    commands = lstToCommands(input)
    pos_H, pos_T = [0, 0], [0, 0]
    visited = set()
    visited.add((pos_H[0], pos_H[1]))
    for command in commands:
        pos_H, pos_T = getNewIndex(command, pos_H, pos_T, visited)
    
    print("Part 1: " + str(len(visited)))

def part2(input):
    commands = lstToCommands(input)
    startingPos = [0, 0]
    pos_H, pos_T = startingPos, [ startingPos for _ in range(9)]
    visited = set()
    visited.add((pos_H[0], pos_H[1]))
    for command in commands:
        # print_matrix(pos_H, pos_T)
        pos_H, pos_T = getNewIndexVariableTail(command, pos_H, pos_T, visited)
    # print_matrix(pos_H, pos_T)
    
    print("Part 2: " + str(len(visited)))

def main():
    input = readInput()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()

