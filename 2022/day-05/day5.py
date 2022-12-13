import re

def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line[:-1])
    return input

def convertInput(input):
    for i in range(0, len(input)):
        if (not input[i]):
            break
    stacksRaw = input[:i-1]
    movesRaw = input[i+1:]
    stacks = [[] for i in range(int(input[i-1].strip()[-1]))]

    for row in stacksRaw:
        idx = 0
        currentLetter = ''
        for i in range(0, len(row), 4):
            try:
                currentLetter = re.search('\[(.+?)\]', row[i:i+4]).group(1) #row[i+1]
            except AttributeError:
                currentLetter = '' 
            if (not currentLetter or currentLetter == ' '):
                idx+=1
                continue
            stacks[idx].append(currentLetter)
            idx+=1
    for stack in stacks:
        stack.reverse()

    moves = []
    for m in movesRaw:
        m = m.replace('move ', '')
        m = m.replace('from ', '')
        m = m.replace('to ', '')
        splits = m.split(' ')
        moves.append({"items":int(splits[0]), "from":int(splits[1])-1, "to":int(splits[2])-1})
    
    return stacks, moves

def part1(raw_input):
    stacks, moves = convertInput(raw_input)

    for move in moves:
        for times in range(move['items']):
            stacks[move['to']].append(stacks[move['from']].pop())

    returnStr = []
    for stack in stacks:
        returnStr.append(stack[-1])
    print("Part 1: " + str(''.join(returnStr)))

def part2(raw_input):
    stacks, moves = convertInput(raw_input)

    for move in moves:
        popped = [stacks[move['from']].pop() for idx in range(move['items'])]
        stacks[move['to']] += popped[::-1]

    returnStr = []
    for stack in stacks:
        returnStr.append(stack[-1])
    print("Part 2: " + str(''.join(returnStr)))


def main():
    input = readInput()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()