dirrections = {
    "forward": [1, 0],
    "down": [0, 1],
    "up": [0, -1],
}
position = [0, 0]

with open("day2_1.txt", "r") as dat:
    for line in dat:
        d, step = line.split(" ")
        step = int(step)

        position[0] += dirrections[d][0] * step
        position[1] += dirrections[d][1] * step

print(position[0] * position[1])     
