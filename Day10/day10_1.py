height_map = []
with open("day10_1.txt", "r") as dat:
    for line in dat:
        heights = list(map(int, list(line.strip(" \n\r"))))
        height_map.append(heights)

def danger_level(height_map, x, y): 
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
            if height_map[y + y_diff][x + x_diff] <= height_map[y][x]:
                return 0
    return height_map[y][x] +1
    
def sum_risk_levels(height_map):
    total = 0
    for y in range(len(height_map)):
        for x in range(len(height_map[0])):
            total += danger_level(height_map, x, y)
    return total

print(sum_risk_levels(height_map))
