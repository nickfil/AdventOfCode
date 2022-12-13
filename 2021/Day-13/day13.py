def findMaxes(dts):
    maxX = 0
    maxY = 0
    for dot in dts:
        maxX = max(dot['x'], maxX)
        maxY = max(dot['y'], maxY)
    return maxX+1, maxY+1

def fillTheHashes(matrix, hashes):
    for each in hashes:
        x = each['x']
        y = each['y']
        matrix[y][x] = '#'
    return matrix


def countHashes(matrix):
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='#':
                counter+=1
    return counter

def fold(matrix, fold, isVertical=True):
    maxY = len(matrix)-1
    maxX = len(matrix[0])-1
    if isVertical:
        for i in range(fold, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='#':
                    newY = maxY-i
                    matrix[newY][j] = '#'
        return matrix[:fold]
    else:
        for i in range(len(matrix)):
            for j in range(fold, len(matrix[0])):
               if matrix[i][j]=='#':
                    newX = maxX-j
                    matrix[i][newX] = '#'
        for i in range(len(matrix)):
            matrix[i] = matrix[i][:fold]
        return matrix


f = open("input.txt", "r")
dots = []
instructions = []
for line in f.readlines():
    if line[0] !='f' and line[0]!='\n':
        line = line.strip().split(',')
        dots.append({'x' : int(line[0]), 'y' : int(line[1])})
    elif line[0]!='\n':
        line = line.split(' ')[-1].strip().split('=')
        instructions.append([line[0], line[1]])

maxXcoord, maxYcoord = findMaxes(dots)
paper = [ [ '.' for i in range(maxXcoord) ] for j in range(maxYcoord) ]

paper = fillTheHashes(paper, dots)
# for p in paper:
#     print(p)
# print(instructions[0][1])
counter=0
for instruction in instructions:
    paper = fold(paper, int(instruction[1]), instruction[0]=='y')
    if counter==0:
        print("Hashes after first fold are: " + str(countHashes(paper)))
        counter+=1
    for p in paper:
        print(p)
    print('-------------------')
print("Hashes after all folds are: " + str(countHashes(paper)))

