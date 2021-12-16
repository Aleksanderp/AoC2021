import heapq

EXPAND = True
grid = []
with open("day15.txt", "r") as dat:
    for line in dat:
        grid.append(list(map(int, list(line.strip("\n\r")))))

if EXPAND:
    # multiple columns
    new_grid = []
    for y in range(len(grid)):
        new_grid.append([])
        for add in range(0, 5):
            for x in range(len(grid)):
                val = grid[y][x] + add
                if val > 9:
                    val -= 9
                new_grid[y].append(val)
    # multiple rows
    for add in range(1, 5):
        for y in range(0, len(grid)):
            new_grid.append([])
            for val in new_grid[y]:
                val = val + add
                if val > 9:
                    val -= 9
                new_grid[-1].append(val)
    grid = new_grid
    
memo = {}
to_check = [(0, 0, 0)]
while len(to_check) > 0:
    x, y, current_risk = heapq.heappop(to_check)
    for n_x, n_y in {(x+1, y), (x-1, y), (x, y-1), (x, y+1)}:
        if n_x < 0 or n_x >= len(grid) or n_y < 0 or n_y >= len(grid):
            continue
        risk = current_risk + grid[n_y][n_x]
        if (n_x, n_y) in memo and memo[(n_x, n_y)] <= risk:
            continue
        memo[(n_x, n_y)] = risk
        heapq.heappush(to_check, (n_x, n_y, risk))
last = len(grid) -1
print(memo[(last, last)])
