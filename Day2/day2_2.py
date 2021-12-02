position = [0, 0]
aim = 0
with open("day2_2.txt", "r") as dat:
    for line in dat:
        dirrection, step = line.split(" ")
        step = int(step)

        if dirrection == "forward":
            position[0] += step
            position[1] += aim * step
        if dirrection == "down":
            aim += step
        if dirrection == "up":
            aim -= step
print(position[0] * position[1])     
