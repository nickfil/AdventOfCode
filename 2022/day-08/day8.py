def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def printMatrix(m):
    for line in m:
        print(line)

def inputToMatrix(lst):
    for i in range(len(lst)):
        lst[i] = list(lst[i])
    return lst

def isVisible(grid, i, j):
    if(i==0 or j==0 or i==len(grid)-1 or j==len(grid[i])-1):
         return True
    
    curValue = grid[i][j]
    left, right, top, bottom = False, False, False, False
    tempIdx = i + 1
    while (tempIdx < len(grid)):
        if (curValue <= grid[tempIdx][j]):
            right = True
        tempIdx += 1
    
    tempIdx = i - 1
    while (tempIdx >= 0):
        if (curValue <= grid[tempIdx][j]):
            left = True
        tempIdx -= 1

    tempIdx = j + 1
    while (tempIdx < len(grid[i])):
        if (curValue <= grid[i][tempIdx]):
            bottom = True
        tempIdx += 1

    tempIdx = j - 1
    while (tempIdx >= 0):
        if (curValue <= grid[i][tempIdx]):
            top = True
        tempIdx -= 1
    
    if (left and right and top and bottom):
        return False
    
    return True

def getScenicScore(grid, i, j):
    if(i==0 or j==0 or i==len(grid)-1 or j==len(grid[i])-1):
         return 0
    
    left, right, top, bottom = 0, 0, 0, 0
    
    curValue = grid[i][j]
    tempIdx = j - 1
    tallestNeighbor = grid[i][tempIdx]
    while (tempIdx >= 0):
        if (tallestNeighbor >= curValue):
            break
        left += 1
        tallestNeighbor = max(grid[i][tempIdx], tallestNeighbor)
        tempIdx -= 1

    tempIdx = j + 1
    tallestNeighbor = grid[i][tempIdx]
    while (tempIdx < len(grid[i])):
        if (tallestNeighbor >= curValue):
            break
        right += 1
        tallestNeighbor = max(grid[i][tempIdx], tallestNeighbor)
        tempIdx += 1

    tempIdx = i - 1
    tallestNeighbor = grid[tempIdx][j]
    while (tempIdx >= 0):
        if (tallestNeighbor >= curValue):
            break
        top += 1
        tallestNeighbor = max(grid[tempIdx][j], tallestNeighbor)
        tempIdx -= 1

    tempIdx = i + 1
    tallestNeighbor = grid[tempIdx][j]
    while (tempIdx < len(grid)):
        if (tallestNeighbor >= curValue):
            break
        bottom += 1
        tallestNeighbor = max(grid[tempIdx][j], tallestNeighbor)
        tempIdx += 1
    
    if left == 0: left+=1
    if right == 0: right+=1
    if top == 0: top+=1
    if bottom == 0: bottom+=1
    # print(curValue, ": ", top, left, bottom, right)
    return left * right * top * bottom

def findVisibleTrees(grid):
    visibles = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (isVisible(grid, i, j)):
                visibles += 1

    return visibles

def findBestScenicScore(grid):
    scenicScores = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            scenicScores.append(getScenicScore(grid, i, j))

    return max(scenicScores)

def part1(input):
    matrix = inputToMatrix(input)
    print("Part 1: " + str(findVisibleTrees(matrix)))

def part2(input):
    matrix = inputToMatrix(input)
    print("Part 2: " + str(findBestScenicScore(matrix)))

def main():
    input = readInput()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()