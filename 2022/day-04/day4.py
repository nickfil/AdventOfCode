def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def convertLinesToListOfRanges(lines):
    res = []
    for line in lines:
        ranges = line.split(',')
        pair1 = ranges[0].split('-')
        pair2 = ranges[1].split('-')
        range1 = range(int(pair1[0]), int(pair1[1])+1)
        range2 = range(int(pair2[0]), int(pair2[1])+1)
        res.append([range1, range2])
    return res

def containsBidi(range1, range2):
    oneContainsTwo = range1.start in range2 and range1[-1] in range2
    twoContainsOne = range2.start in range1 and range2[-1] in range1
    return oneContainsTwo or twoContainsOne

def overlaps(range1, range2):
    return range1.start <= range2[-1] and range1[-1] >= range2.start

def part1(input):
    listOfRanges = convertLinesToListOfRanges(input)
    counter = 0
    for rangePair in listOfRanges:
        if (containsBidi(rangePair[0], rangePair[1])):
            counter += 1
        
    print('Part 1: ' + str(counter))

def part2(input):
    listOfRanges = convertLinesToListOfRanges(input)
    counter = 0
    for rangePair in listOfRanges:
        if (overlaps(rangePair[0], rangePair[1])):
            counter += 1
        
    print('Part 2: ' + str(counter))

def main():
    input = readInput()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()