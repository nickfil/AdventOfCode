import string

ALPHABET_MAP = { letter:idx+1 for idx, letter in enumerate(list(string.ascii_lowercase) + list(string.ascii_uppercase)) }

def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def convertToCompartments(lst):
    res = []
    for item in lst:
        compartmentSize = int(len(item) / 2)
        res.append([item[:compartmentSize], item[compartmentSize:]])
    return res

def convertToTeams(lst):
    res = []
    for i in range(0, len(lst), 3):
        res.append([lst[i], lst[i+1], lst[i+2]])
    return res

def findDuplicate(listOfStrings):
    listOfSets = [ set(lst) for lst in listOfStrings]
    u = set.intersection(*listOfSets)
    return u.pop()

def part1(input):
    comparments = convertToCompartments(input)
    
    duplicates = []
    for c in comparments:
        duplicates.append(findDuplicate(c))

    total = 0
    for dup in duplicates:
        total += ALPHABET_MAP[dup]
    
    print('Part 1: ' + str(total))

def part2(input):
    teams = convertToTeams(input)

    duplicates = []
    for team in teams:
        duplicates.append(findDuplicate(team))
    
    total = 0
    for dup in duplicates:
        total += ALPHABET_MAP[dup]
    
    print('Part 2: ' + str(total))

def main():
    input = readInput()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()