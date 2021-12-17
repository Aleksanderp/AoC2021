
with open("day17.txt", "r") as dat:
    x_y = dat.readline().strip("\n\r").split(":")[1].replace(" x=", "").replace(" y=", "")
    x_bound, y_bound = x_y.split(",")
    x_bound = tuple(map(int, x_bound.split("..")))
    y_bound = tuple(map(int, y_bound.split("..")))

def end_position(speed, steps):
    return steps * (2 * speed - steps + 1) / 2

def x_hits_target(speed, upper, lower):
    steps = []
    for s in range(0, speed +1):
        pos = end_position(speed, s)
        if pos >= lower and pos <= upper:
            steps.append(s if s != speed else None)
    return steps


def x_speed_min_max_steps(x_bound):
    x_valid = []
    for x_initital in range(0, x_bound[1] +1):
        steps= x_hits_target(x_initital, x_bound[1], x_bound[0])
        if len(steps) > 0:
            x_valid.append((steps[0], steps[-1]))
    return x_valid

def y_hits_target(speed, upper, lower):
    steps = []
    pos = 0
    step = 0
    max_y = 0
    while pos > lower:
        pos += speed
        speed -= 1
        step += 1
        if pos > max_y:
            max_y = pos
        if pos >= lower and pos <= upper:
            steps.append(step)
    return steps, max_y

def y_speed_min_max_steps(y_bound):
    y_valid = []
    max_y = 0
    for y_initial in range(y_bound[0], 1000):
        steps, y = y_hits_target(y_initial, y_bound[1], y_bound[0])
        if len(steps) > 0:
            if y > max_y:
                max_y = y
            y_valid.append((steps[0], steps[-1]))
    return y_valid, max_y

x_steps = x_speed_min_max_steps(x_bound)
y_steps, max_y = y_speed_min_max_steps(y_bound)
print("Part 1 [Max Y: {}]".format(max_y))
total = 0
for x_min, x_max in x_steps:
    for y_min, y_max in y_steps:
        if (x_max is None or y_min <= x_max) and x_min <= y_max:
            total += 1
print("Part 2 [Valid initial velocities: {}]".format(total))
