import copy
import time
import math

def readInput():
    f = open("test-input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def makeInputEasierToUse(input):
    res = []
    
    for i in range(0, len(input), 7):
        dic = {}
        temp = input[i+1].replace('Starting items: ', '').split(', ')
        dic['startingItems'] = [ int(item) for item in temp ]
        temp = input[i+2].replace('Operation: ', '').split(' ')
        dic['operation'] = { 'symbol': temp[3], 'value': temp[4] }
        dic['test'] = int(input[i+3].replace('Test: divisible by ', ''))
        dic['ifTrue'] = int(input[i+4].replace('If true: throw to monkey ', ''))
        dic['ifFalse'] = int(input[i+5].replace('If false: throw to monkey ', ''))
        dic['itemsInspected'] = 0

        res.append(dic)
    return res

def performOperation(symbol, value1, value2):
    if symbol == '*':
        return value1 * value2
    
    return value1 + value2
        
def part1(input):
    rounds = []

    for i in range(20):
        for monkey in input:
            while monkey['startingItems']:
                curItem = monkey['startingItems'].pop(0)
                monkey['itemsInspected'] += 1
                secondItem = None
                if monkey['operation']['value'] == 'old':
                    secondItem = curItem
                else:
                    secondItem = int(monkey['operation']['value'])
                
                new = performOperation(monkey['operation']['symbol'], curItem, secondItem)
                boredScore = new // 3
                isDivisibleByTest = boredScore % monkey['test'] == 0
                
                monkeyToAddItem = None
                if isDivisibleByTest:
                    monkeyToAddItem = monkey['ifTrue']
                else:
                    monkeyToAddItem = monkey['ifFalse']
                
                input[monkeyToAddItem]['startingItems'].append(boredScore)
        rounds.append(copy.deepcopy(input))
    
    for i, round in enumerate(rounds):
        print('Round ', i)
        for idx, monkey in enumerate(round):
            print("Monkey ", idx, ': ', monkey['startingItems'], '| Inspected: ', monkey['itemsInspected'])
        print('----------------------')

    finalRoundInspections = []
    for monkey in rounds[-1]:
        finalRoundInspections.append(monkey['itemsInspected'])
    finalRoundInspections.sort()
    print("Part 1: ", finalRoundInspections[-1]*finalRoundInspections[-2])
    
def part2(input):
    rounds = []

    for i in range(10000):
        allnums = []
        for monkey in input:
            allnums.append(monkey['test'])
        supermod = math.prod(allnums)
        for monkey in input:
            while monkey['startingItems']:
                curItem = monkey['startingItems'].pop()
                
                monkey['itemsInspected'] += 1
                secondItem = None
                if monkey['operation']['value'] == 'old':
                    secondItem = curItem
                else:
                    secondItem = int(monkey['operation']['value'])
                
                new = performOperation(monkey['operation']['symbol'], curItem, secondItem) % supermod
                isDivisibleByTest = new % monkey['test'] == 0

                monkeyToAddItem = None
                if isDivisibleByTest:
                    monkeyToAddItem = monkey['ifTrue']
                else:
                    monkeyToAddItem = monkey['ifFalse']
                
                input[monkeyToAddItem]['startingItems'].append(new)
                
        itemCounts = []
        for monkey in input:
            itemCounts.append(monkey['itemsInspected'])
        rounds.append(itemCounts)

    finalRoundInspections = sorted(rounds[-1])
    print("Part 2: ", finalRoundInspections[-1]*finalRoundInspections[-2])

def main():
    input = readInput()
    betterInput = makeInputEasierToUse(input)
    part1(copy.deepcopy(betterInput))
    part2(copy.deepcopy(betterInput))

if __name__ == "__main__":
    main()