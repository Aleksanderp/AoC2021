boards_numbers_positions = []
boards_position_numbers = []

with open("day4_1.txt", "r") as dat:
    numbers = dat.readline()
    y = 0
    for line in dat:
        line = line.strip("\n\r ").replace("  ", " ")
        if line == "":
            y = 0
            boards_numbers_positions.append({})
            boards_position_numbers.append({})
            continue
        x = 0
        for num in line.split(" "):
            boards_numbers_positions[-1][num] = (x, y)
            boards_position_numbers[-1][(x, y)] = num
            x += 1
        y += 1

def isBingo(board_positions, pos):
    bingo = True
    for x in range(5):
        if board_positions.get((x, pos[1])) != None:
            bingo = False
            break
    if bingo:
        return True

    bingo = True
    for y in range(5):
        if board_positions.get((pos[0], y)) != None:
            bingo = False
            break
    return bingo

w_board = None
last_num = None
for n in numbers.split(","):
    for b in range(len(boards_numbers_positions)):
        pos = boards_numbers_positions[b].pop(n, None)
        if pos == None:
            continue
        boards_position_numbers[b].pop(pos)
        if isBingo(boards_position_numbers[b], pos):
            w_board = b
            break
            
    if w_board != None:
        last_num = int(n)
        break

def calculate_winning_score(board_numbers, last_num):
    total = 0
    for n in board_numbers.keys():
        total += int(n)
    return total * last_num


print(w_board)
if w_board != None: # pylance
    print(calculate_winning_score(boards_numbers_positions[w_board], last_num))
