ones_counts = []
line_count = 0

with open("day3_1.txt", "r") as dat:
    for line in dat:
        bits = list(line.strip("\n\r"))
        for i in range(len(bits)):
            if i == len(ones_counts):
                ones_counts.append(0)
            if bits[i] == "1":
                ones_counts[i] += 1
        line_count += 1

gamma = 0
epsilon = 0
for i in range(len(ones_counts)):
    gamma = gamma << 1
    epsilon = epsilon << 1
    if ones_counts[i] >= line_count / 2:
        gamma += 1
    else:
        epsilon += 1
print(gamma * epsilon)
