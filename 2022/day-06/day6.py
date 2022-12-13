def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def findSeq(inputStr, seqLen):
    for i in range(len(inputStr) - seqLen):
        if (len(set(inputStr[i:i+seqLen])) == seqLen):
            return i + seqLen
    return 0

def part1(input):
    res = findSeq(input[0], 4)
    print("Part 1: " + str(res))

def part2(input):
    res = findSeq(input[0], 14)
    print("Part 2: " + str(res))

def main():
    input = readInput()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()