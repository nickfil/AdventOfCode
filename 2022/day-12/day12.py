class Node():
    def __init__(self, i, j, letter):
        self.i = i
        self.j = j
        self.letter = letter
        self.distance = float("inf")

def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(list(line.strip()))
    return input

def printGrid(grid):
    for row in grid:
        for c in row:
            print(c.distance, end = ' ')
        print('')

def find(grid, char):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == char:
                return [i,j]

def createObjGrid(input):
    newGrid = [['' for _ in range(len(input[0]))] for _ in range(len(input))]
    for i in range(len(input)):
        for j in range(len(input[0])):
            newGrid[i][j] = Node(i, j, input[i][j])
    return newGrid

def getNeighbors(node, grid):
    all = [ [node.i+1,  node.j], [node.i-1, node.j], [node.i, node.j+1], [node.i, node.j-1] ]
    res = []
    for each in all:
        if (each[0]<0 or each[0]>=len(grid) or each[1]<0 or each[1]>=len(grid[0])):
            continue

        if ord(grid[each[0]][each[1]].letter) - ord(node.letter) <= 1:
            res.append(grid[each[0]][each[1]])
        if node.letter == 'z' and grid[each[0]][each[1]].letter == 'E':
            res.append(grid[each[0]][each[1]])
        if node.letter == 'S' and grid[each[0]][each[1]].letter == 'a':
            res.append(grid[each[0]][each[1]])
    return res

def bfs(start, end, grid):
    grid[start[0]][start[1]].distance = 0
    grid[start[0]][start[1]].letter = 'a'
    grid[end[0]][end[1]].letter = 'z'
    q = []
    q.append(grid[start[0]][start[1]])

    while q:
        cur = q.pop(0)
        neighbors = getNeighbors(cur, grid)
        for neighbor in neighbors:
            if neighbor.distance == float('inf'):
                neighbor.distance = cur.distance + 1
                q.append(neighbor)
    
    return grid[end[0]][end[1]]

def part1(input):
    start = find(input, 'S')
    end = find(input, 'E')
    grid = createObjGrid(input)
    
    print("Part 1: ", bfs(start, end, grid).distance)
    
def part2(input):
    start = find(input, 'S')
    startingPoints = [start]
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'a':
                startingPoints.append([i, j])
    end = find(input, 'E')
    grid = createObjGrid(input)

    distances = []
    for each in startingPoints:
        distances.append(bfs(each, end, createObjGrid(input)).distance)
    
    print("Part 1: ",min(distances))


def main():
    input = readInput()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()