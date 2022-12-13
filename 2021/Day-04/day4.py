def clean_list(lst):
    retList = []
    for item in lst:
        if (item != ''):
            retList.append(int(item))
    return retList

def check_winner(board):
    # check rows
    for row in board:
        r = all(flag == -1 for flag in row)
        if r: return True
    
    # check columns
    for col in range(len(board[0])):
        cur_column = []
        for row in board:
            cur_column.append(row[col])
        r = all(flag == -1 for flag in cur_column)
        if r: return True
    
    return False

def mark_board(board, number):
    # print("before: " + str(board))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == number):
                board[i][j] = -1
    # print("after: " + str(board))
    return board

def calculate_score(board, number):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] != -1):
                score+=board[i][j]
    return score*number

f = open("input.txt", "r")
numbers_1 = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
numbers = [26,55,7,40,56,34,58,90,60,83,37,36,9,27,42,19,46,18,49,52,75,17,70,41,12,78,15,64,50,54,2,77,76,10,43,79,22,32,47,0,72,30,21,82,6,95,13,59,16,89,1,85,57,62,81,38,29,80,8,67,20,53,69,25,23,61,86,71,68,98,35,31,4,33,91,74,14,28,65,24,97,88,3,39,11,93,66,44,45,96,92,51,63,84,73,99,94,87,5,48]
bingo_boards = {}
current_board = []
index=0
for line in f.readlines():
    if (line == '\n'):
        bingo_boards[index] = current_board
        index+=1
        current_board = []
    else:
        cur_list = clean_list(list(line.split(' ')))
        current_board.append(cur_list)
bingo_boards[index] = current_board
initial_size = len(bingo_boards)

# board ready - Lets play some bingo!

losing_board = []
losing_number = -1
for number in numbers:
    indexes_to_pop = []
    for i in bingo_boards:
        board = mark_board(bingo_boards[i], number)
        bingo_boards[i] = board
        if (check_winner(bingo_boards[i])):
            winning_board = bingo_boards[i]
            winning_number = number
            if (len(bingo_boards) == 1):
                print("Score of the losing board is: " + str(calculate_score(winning_board, winning_number)))
                break
            elif (len(bingo_boards) == initial_size):
                print("Score of the first winning board is: " + str(calculate_score(winning_board, winning_number)))
            indexes_to_pop.append(i)
    else:
        for index in indexes_to_pop:
            bingo_boards.pop(index)
        continue
    break
    
