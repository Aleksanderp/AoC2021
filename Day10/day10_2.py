height_map = []
with open("day10_2.txt", "r") as dat:
    for line in dat:
        heights = list(map(int, list(line.strip(" \n\r"))))
        height_map.append(heights)
checked = [[False for _ in range(len(height_map[0]))] for _ in range(len(height_map))]

def basin_size(x, y): 
    if checked[y][x]:
        return 0
    checked[y][x] = True
    if height_map[y][x] == 9:
        return 0

    total_size = 0
    for y_diff in range(-1, 2):
        for x_diff in range(-1, 2):
            if x_diff != 0 and y_diff != 0:
                continue
            if x_diff == y_diff:
                continue
            if x + x_diff < 0 or x + x_diff >= len(height_map[0]):
                continue
            if y + y_diff < 0 or y + y_diff >= len(height_map):
                continue
            total_size += basin_size(x + x_diff, y + y_diff)
           
    return 1 + total_size

basin_sizes = []
for y in range(0, len(height_map)):
    for x in range(0, len(height_map[0])):
        if checked[y][x]:
            continue
        basin_sizes.append(basin_size(x, y))

result = 1
for bs in sorted(basin_sizes, reverse=True)[0:3]:
    result *= bs
print(result)
