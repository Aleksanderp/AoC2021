boards_numbers_positions = []
boards_position_numbers = []

with open("day4_2.txt", "r") as dat:
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

def isBingo(boards_positions, pos):
    bingo = True
    for x in range(5):
        if boards_positions.get((x, pos[1])) != None:
            bingo = False
            break
    if bingo:
        return True

    bingo = True
    for y in range(5):
        if boards_positions.get((pos[0], y)) != None:
            bingo = False
            break
    return bingo

w_boards = []
last_num = None
for n in numbers.split(","):
    for b in range(len(boards_numbers_positions)):
        if b in w_boards:
            continue

        pos = boards_numbers_positions[b].pop(n, None)
        if pos == None:
            continue
        boards_position_numbers[b].pop(pos)
        if isBingo(boards_position_numbers[b], pos):
            w_boards.append(b)

    if len(w_boards) == len(boards_numbers_positions):
        last_num = int(n)
        break

def calculate_winning_score(board_numbers, last_num):
    total = 0
    for n in board_numbers.keys():
        total += int(n)
    return total * last_num


print(w_boards[-1])
print(calculate_winning_score(boards_numbers_positions[w_boards[-1]], last_num))
