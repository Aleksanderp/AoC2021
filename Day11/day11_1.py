STEPS = 100
octopuses = []
flashes = 0
with open("day11_1.txt", "r") as dat:
    for line in dat:
        octopuses.append(list(map(int, list(line.strip("\n\r")))))

def flash(have_flashed, x, y):
    if (x,y) in have_flashed:
        return 0
    if octopuses[y][x] <= 9:
        return 0
    have_flashed.add((x,y))
    flashes = 0
    for y_diff in range(-1, 2):
        for x_diff in range(-1, 2):
            if y_diff == 0 and x_diff == 0:
                continue
            if y + y_diff < 0 or y + y_diff >= len(octopuses):
                continue
            if x + x_diff < 0 or x + x_diff >= len(octopuses[0]):
                continue
            octopuses[y + y_diff][x + x_diff] += 1
            flashes += flash(have_flashed, x + x_diff, y + y_diff)
    return flashes + 1 

for _ in range(0, STEPS):
    have_flashed = set()
    will_flash = []
    for y in range(len(octopuses)):
        for x in range(len(octopuses[0])):
            octopuses[y][x] += 1
            if octopuses[y][x] > 9:
                will_flash.append((x, y))
    for x, y in will_flash:
        flashes += flash(have_flashed, x, y)
    for x, y in have_flashed:
        octopuses[y][x] = 0
print(flashes)
