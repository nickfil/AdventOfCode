from functools import cmp_to_key
def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        if line.strip():
            input.append(eval(line.strip()))
    return input

def lstToLstOfPairs(input):
    res = []
    for i in range(1, len(input), 2):
        res.append([input[i-1], input[i]])
    return res

# right is first: -1
# left is first: 1
# right and left are equal: 0
def order(first, second):
    if not first and second: return -1
    elif first and not second: return 1
    if (type(first) is int and type(second) is int):
        if first < second: return -1
        elif first == second: return 0
        else: return 1
    elif(type(first) is list and type(second) is int):
        return order(first, [second])
    elif(type(first) is int and type(second) is list):
        return order([first], second)
    
    for i in range(max(len(first), len(second))):
        if i >= len(first): return -1
        elif i >= len(second): return 1

        curOrder = order(first[i], second[i])
        if curOrder != 0:
            return curOrder
    return 0

def part1(input):
    correctOrderPairs = []
    for idx, pair in enumerate(input):
        if order(pair[0], pair[1]) == -1:
            correctOrderPairs.append(idx+1)

    print("Part 1: ", sum(correctOrderPairs))

def part2(input):
    divider1 = [[2]]
    divider2 = [[6]]
    individuals = [divider1, divider2]
    for pair in input:
        individuals.append(pair[0])
        individuals.append(pair[1])

    individuals.sort(key=cmp_to_key(order))
    pos1, pos2 = 1, 1
    for i in range(len(individuals)):
        if individuals[i] == divider1:
            pos1 += i
        elif individuals[i] == divider2:
            pos2 += i
    
    print("Part 2: ", pos1*pos2)


def main():
    input = readInput()
    lst = lstToLstOfPairs(input)
    part1(lst)
    part2(lst)

if __name__ == "__main__":
    main()