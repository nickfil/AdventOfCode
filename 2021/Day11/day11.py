adjacents = [[0,1], [0,-1], [1,0], [-1,0], [-1,-1], [-1,1], [1,-1], [1,1]]
def isValid(matrix, i, j):
    if i >= len(matrix) or i < 0 or j >= len(matrix[0]) or j < 0:
        return False
    return True

def getFlashed(matrix):
    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j]==0):
                c+=1
    return c

def calculateFlashes(matrix, i, j, flashedPos):
    if (not flashedPos[i][j] and matrix[i][j] < 9):
        matrix[i][j] += 1
    elif (not flashedPos[i][j] and matrix[i][j] == 9):
        matrix[i][j] = 0
        flashedPos[i][j] = True
        for each in adjacents:
            if isValid(matrix, i+each[0], j+each[1]):
                calculateFlashes(matrix, i+each[0], j+each[1], flashedPos)
    return matrix

def allFlashesSync(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                return False
    return True

f = open("input.txt", "r")
octopuses = []
for line in f.readlines():
    octopuses.append([int(char) for char in line.strip()])

step = 1
counter = 0

while True:
    flashed = [[False for i in range(len(octopuses[0]))] for j in range(len(octopuses))]
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            octopuses = calculateFlashes(octopuses, i, j, flashed)
    # print("Step " + str(step+1) + ": " + str(octopuses))
    counter += getFlashed(octopuses)

    if step == 100:
        print("Sum of flashes at step 100 is: " + str(counter))

    if allFlashesSync(octopuses):
        print("Step where all flashes sync is: " + str(step))
        break
    step+=1