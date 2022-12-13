import math
def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def part1(input):
    mem = [0]
    x, execCycle = 1, 1
    while(True):
        if not input:
            break
        curInput = input.pop(0)
        if curInput == 'noop':
            mem.append(execCycle*x)
            execCycle += 1
            continue
        
        splitInput = curInput.split(' ')
        curInstruction = splitInput[0]
        curValue = int(splitInput[1])
        if curInstruction == 'addx':
            # initial cycle - previous command completes, current command starts executing
            mem.append(execCycle*x)
            execCycle+=1

            # in between cycle - nothing happens
            mem.append(execCycle*x)
            execCycle+=1

            # second add cycle - can now increment x
            x += curValue

    idxs = [20, 60, 100, 140, 180, 220]
    total = 0
    for idx, val in enumerate(mem):
        if idx in idxs:
            total += val
    
    print("Part 1: ", total)

def getXForEachCycle(input):
    mem = [1]
    x, execCycle = 1, 1
    while(True):
        if not input:
            break
        curInput = input.pop(0)
        if curInput == 'noop':
            mem.append(x)
            execCycle += 1
            continue
        
        splitInput = curInput.split(' ')
        curInstruction = splitInput[0]
        curValue = int(splitInput[1])
        if curInstruction == 'addx':
            # initial cycle - previous command completes, current command starts executing
            mem.append(x)
            execCycle+=1

            # in between cycle - nothing happens
            mem.append(x)
            execCycle+=1

            # second add cycle - can now increment x
            x += curValue
    
    return mem

def part2(input):
    board = [['.' for _ in range(40)] for _ in range(6)]
    xs = getXForEachCycle(input)
    xs.pop(0)
    for idx, value in enumerate(xs):
        row = idx // 40
        column = idx % 40
        if value-1 <= column <= value+1:
            board[row][column] = '#'

    for row in board:
        print(''.join(row))
    
    print("Part 2: ", "PLULKBZH")

def main():
    input = readInput()
    part1(input.copy())
    part2(input.copy())

if __name__ == "__main__":
    main()