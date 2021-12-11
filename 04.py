from sys import stdin
from pprint import pprint
numbers = [int(num) for num in stdin.readline().rstrip().split(',')]

#print(numbers)

score = 0

boards = []
board_count=-1
for line in stdin:
    if line == '\n':
        board_count+=1
        boards.append([])
    else:
        row = [(int(num),0) for num in line.rstrip().split()]
        boards[board_count].append(row)

won_boards = [0 for _ in range(board_count+1)]

print(board_count)
print(won_boards)

#pprint(boards)

def check(number, boards):

    # check across
    check_win(number, boards)

    tr_boards = boards.copy()
    for board in range(len(tr_boards)):
        tr_boards[board] = list(zip(*tr_boards[board]))

    #check across on transpose
    check_win(number, tr_boards)

def check_win(number, boards):
    #check across
    global score
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            count = 0
            for col in range(len(boards[board][row])):
                if boards[board][row][col][1]==1:
                    count+=1
            if count == 5:
                #print('winner exit')
                #pprint(boards[board])
                unmarked_numbers_sum = 0
                for row in boards[board]:
                    for col in row:
                        if col[1] == 0:
                            unmarked_numbers_sum+=col[0]
                print(unmarked_numbers_sum, number)
                print(unmarked_numbers_sum * number)
                won_boards[board] = 1
                if won_boards.count(1) == len(won_boards):
                    exit()
                    

for number in numbers:
    #print(number)
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for col in range(len(boards[board][row])):
                if number==boards[board][row][col][0]:
                    boards[board][row][col] = (number,1)
    check(number, boards)

pprint(boards)
print(score)