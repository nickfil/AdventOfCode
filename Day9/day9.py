from collections import deque as queue
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]
def isValid(vis, row, col):
   
    if (row < 0 or col < 0 or row >= len(vis) or col >= len(vis[0])):
        return False
 
    if (vis[row][col]):
        return False
 
    return True
 
def calculateBasinSizeFromLowPoint(grid, vis, row, col):
    q = queue()
 
    q.append(( row, col ))
    vis[row][col] = True
 
    size = 0
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        size+=1
 
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy) and grid[adjx][adjy] != 9):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
    return size

def isLowPoint(matrix, x, y):
    pointsToCheck = []
    if (x > 0):
        pointsToCheck.append({'x': x-1, 'y':y})
    if (y > 0):
        pointsToCheck.append({'x': x, 'y':y-1})
    if (x < len(matrix)-1):
        pointsToCheck.append({'x': x+1, 'y':y})
    if ( y < len(matrix[0])-1):
        pointsToCheck.append({'x': x, 'y':y+1})

    currentPoint = matrix[x][y]
    for p in pointsToCheck:
        if matrix[p['x']][p['y']] <= currentPoint:
            return False
    return True

f = open("input.txt", "r")
heights_matrix = []
for line in f.readlines():
    heights_matrix.append([int(char) for char in line.strip()])

# matrix ready, let's do some calculations
counter=0
basinSizes=[]
visited = [[ False for i in range(len(heights_matrix[0]))] for i in range(len(heights_matrix))]
for i in range(len(heights_matrix)):
    for j in range(len(heights_matrix[0])):
        if isLowPoint(heights_matrix, i, j):
            counter+=heights_matrix[i][j]+1
            basinSizes.append(calculateBasinSizeFromLowPoint(heights_matrix, visited, i, j))
basinSizes.sort()

print("Number of low points: " + str(counter))
print("Size of 3 largest basins: " + str(basinSizes[-1]*basinSizes[-2]*basinSizes[-3]))
