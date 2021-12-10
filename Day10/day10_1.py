from os import error

closing_to_opening = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
error_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
with open("day10_1.txt", "r") as program:
    error_score_sum = 0
    for line in program:
        charachters = []
        valid = True
        for c in line.strip("\n\r"):
            if closing_to_opening.get(c) != None:
                if len(charachters) == 0 or charachters[-1] != closing_to_opening.get(c):
                    error_score_sum += error_score[c]
                    break
                charachters.pop(-1)
            else:
                charachters.append(c)
print(error_score_sum)
