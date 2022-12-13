SHAPE_SCORES = {
    "A": 1,
    "B": 2,
    "C": 3
}

CONVERT_XYZ_TO_ABC = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

# Returns the points awarded to index 1
CALCULATE_PLAYER_2_OUTCOME_POINTS = {
    ('A', 'A'): 3, # Draw
    ('A', 'B'): 6, # Win
    ('A', 'C'): 0, # Loss
    ('B', 'A'): 0,
    ('B', 'B'): 3,
    ('B', 'C'): 6,
    ('C', 'A'): 6,
    ('C', 'B'): 0,
    ('C', 'C'): 3
}

# Returns the points awarded to index
CALCULATE_PLAYER_2_SYMBOL = {
    ('A', 'X'): 'C', # X means loss
    ('A', 'Y'): 'A', # Y means draw
    ('A', 'Z'): 'B', # Z means win
    ('B', 'X'): 'A',
    ('B', 'Y'): 'B',
    ('B', 'Z'): 'C',
    ('C', 'X'): 'B',
    ('C', 'Y'): 'C',
    ('C', 'Z'): 'A'
}

def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def convertListToTuples(lst):
    newList = []
    for item in lst:
        splitItems = item.split(' ')
        newList.append((splitItems[0], splitItems[1]))
    return newList

def main():
    input = readInput()
    rounds = convertListToTuples(input)
    totalScore = 0
    totalScore_part2 = 0
    for round in rounds:
        currentTuple = (round[0], CONVERT_XYZ_TO_ABC[round[1]])
        roundScore = CALCULATE_PLAYER_2_OUTCOME_POINTS[currentTuple] + SHAPE_SCORES[currentTuple[1]]
        totalScore += roundScore

        currentTuple2 = (round[0], CALCULATE_PLAYER_2_SYMBOL[round])
        round2Score = CALCULATE_PLAYER_2_OUTCOME_POINTS[currentTuple2] + SHAPE_SCORES[currentTuple2[1]]
        totalScore_part2 += round2Score
    
    print('Part 1: ' + str(totalScore))
    print('Part 2: ' + str(totalScore_part2))

if __name__ == "__main__":
    main()