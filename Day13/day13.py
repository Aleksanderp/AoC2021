def foldPaper(dots, direction, cordinate):
    changed = 0
    if direction == "y":
        changed = 1
    fixed = (changed +1) %2
    new_dots = set()
    for d in dots:
        if d[changed] > cordinate:
            new_dot = [0,0]
            new_dot[changed] = cordinate - (d[changed] - cordinate)
            new_dot[fixed] = d[fixed]
            new_dots.add(tuple(new_dot))
        else:
            new_dots.add(d)
    return new_dots

def printDots(dots, max_x, max_y):
    for y in range(1 + max_y):
        for x in range(1 + max_x):
            print("#", end="") if (x, y) in dots else print(".", end="")
        print("")

# Part 1: FOLD_LIMIT = 1
# Part 2: FOLD_LIMIT = None
FOLD_LIMIT = None
with open("day13.txt", "r") as dat:
    fold = False
    dots = set()
    max_x = None
    max_y = None
    for line in dat:
        line = line.strip("\n\r")
        if line == "":
            fold = True
            continue
        
        if fold:
            direction, cordinate = line.split(" ")[-1].split("=")
            dots = foldPaper(dots, direction, int(cordinate))
            if direction == "x" and (max_x == None or int(cordinate) < max_x):
                max_x = int(cordinate)
            if direction == "y" and (max_y == None or int(cordinate) < max_y):
                max_y = int(cordinate)
            if FOLD_LIMIT != None:
                break
        else:
            x, y = list(map(int, line.split(",")))
            dots.add((x, int(y)))
    if FOLD_LIMIT == None:
        printDots(dots, max_x, max_y)
    print(len(dots))
