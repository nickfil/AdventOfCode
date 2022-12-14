import copy
SAND_STARTING_POINT = { 'x': 500, 'y':0 }
def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def constructCaves(input):
    matrix = [['.' for _ in range(1000)] for _ in range(500)]
    for line in input:
        line = line.split(' -> ')
        for i in range(1, len(line)):
            point1 = line[i-1].split(',')
            point1 = { 'x': int(point1[0]), 'y':int(point1[1]) }
            point2 = line[i].split(',')
            point2 = { 'x': int(point2[0]), 'y':int(point2[1]) }

            isHorizontal = point1['x'] == point2['x']

            startIdx, endIdx = None, None
            if isHorizontal:
                startIdx = min(point1['y'], point2['y'])
                endIdx = max(point1['y'], point2['y'])
            else:
                startIdx = min(point1['x'], point2['x'])
                endIdx = max(point1['x'], point2['x'])
            
            for i in range(startIdx, endIdx+1):
                if isHorizontal:
                    matrix[i][point1['x']] = '#'
                else:
                    matrix[point1['y']][i] = '#'
    return matrix

def findLowestRockY(matrix):
    y = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#' and i > y:
                y = i
    return y

def printMatrix(matrix):
    for line in matrix[0:11]:
        print(line[490:515])

def part1(matrix):
    sandCoords = { 'x': SAND_STARTING_POINT['x'], 'y':SAND_STARTING_POINT['y']+2 }
    matrix[SAND_STARTING_POINT['y']][SAND_STARTING_POINT['x']] = '+'
    lowestRockY = findLowestRockY(matrix)
    counter = 0
    found = False
    
    while sandCoords['y'] < lowestRockY:
        sandCoords = { 'x': SAND_STARTING_POINT['x'], 'y':SAND_STARTING_POINT['y']+1 }
        
        while True:
            if sandCoords['y']+1 > lowestRockY:
                found = True
                break
            elif matrix[sandCoords['y']+1][sandCoords['x']] == '.' :
                sandCoords['y'] += 1
            elif matrix[sandCoords['y']+1][sandCoords['x']-1] == '.':
                sandCoords['y'] += 1
                sandCoords['x'] -= 1
            elif matrix[sandCoords['y']+1][sandCoords['x']+1] == '.':
                sandCoords['y'] += 1
                sandCoords['x'] += 1
            else:
                break
            
        if found: break

        matrix[sandCoords['y']][sandCoords['x']] = 'o'
        counter += 1
    
    print("Part 1: ", counter)
    

def part2(matrix):
    sandCoords = { 'x': SAND_STARTING_POINT['x'], 'y':SAND_STARTING_POINT['y']+1 }
    matrix[SAND_STARTING_POINT['y']][SAND_STARTING_POINT['x']] = '+'
    lowestRockY = findLowestRockY(matrix) + 2
    counter = 0

    while sandCoords['y'] != SAND_STARTING_POINT['y'] or sandCoords['x'] != SAND_STARTING_POINT['x']:
        sandCoords = { 'x': SAND_STARTING_POINT['x'], 'y':SAND_STARTING_POINT['y'] }
        
        while True:
            if sandCoords['y']+1 >= lowestRockY:
                break
            elif matrix[sandCoords['y']+1][sandCoords['x']] == '.' :
                sandCoords['y'] += 1
            elif matrix[sandCoords['y']+1][sandCoords['x']-1] == '.':
                sandCoords['y'] += 1
                sandCoords['x'] -= 1
            elif matrix[sandCoords['y']+1][sandCoords['x']+1] == '.':
                sandCoords['y'] += 1
                sandCoords['x'] += 1
            else:
                break
            
            
        matrix[sandCoords['y']][sandCoords['x']] = 'o'
        counter += 1

    print("Part 2: ", counter)


def main():
    input = constructCaves(readInput())
    part1(copy.deepcopy(input))
    part2(copy.deepcopy(input))

if __name__ == "__main__":
    main()
