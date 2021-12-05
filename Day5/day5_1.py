lines = []

class Point:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]

with open("day5_2.txt", "r") as dat:
    for line in dat:
        points = line.split(" -> ")
        p1 = tuple(map(lambda x: int(x), points[0].split(",")))
        p2 = tuple(map(lambda x: int(x), points[1].split(",")))
        lines.append((Point(p1), Point(p2)))

N = 1000 # input numbers are < 1000 and we can afford that kind of space :D
diagonal = True
grid = [[0 for i in range(N)] for j in range(N)]

def count_intersects(grid, x, x_step, y, y_step, steps):
    new_intersects = 0
    for _ in range(steps):
        grid[x][y] += 1
        if  grid[x][y] == 2:
            new_intersects += 1
        x += x_step
        y += y_step
    return new_intersects

total = 0
for l in lines:
    x_step = -1 if l[0].x > l[1].x else (0 if l[0].x == l[1].x else 1)
    y_step = -1 if l[0].y > l[1].y else (0 if l[0].y == l[1].y else 1)
    if (l[0].x != l[1].x) and (l[0].y != l[1].y):
        if not diagonal:
            continue
        # move diagonally
        total += count_intersects(grid, l[0].x, x_step,  l[0].y, y_step, abs(l[0].x - l[1].x) +1)
    else:
        # move horizontally or vertically
        steps = max(abs(l[0].x - l[1].x), abs(l[0].y - l[1].y)) +1
        total += count_intersects(grid, l[0].x, x_step,  l[0].y, y_step, steps)
print(total)
