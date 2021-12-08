valid_lengths = [2, 4, 3, 7]
total = 0
with open("day8_1.txt", "r") as dat:
    for line in dat:
        output = line.split(" | ")[1].strip("\n\r ")
        for digit in output.split(" "):
            if len(digit) in valid_lengths:
                total += 1
print(total)
