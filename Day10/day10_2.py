from os import error

closing_to_opening = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
error_score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}
with open("day10_2.txt", "r") as program:
    ac_scores = []
    for line in program:
        charachters = []
        valid = True
        for c in line.strip("\n\r"):
            if closing_to_opening.get(c) != None:
                if len(charachters) == 0 or charachters[-1] != closing_to_opening.get(c):
                    valid = False
                    break
                charachters.pop(-1)
            else:
                charachters.append(c)
        if valid:
            line_ac_score = 0
            for idx in range(len(charachters) -1, -1, -1):
                line_ac_score *= 5
                line_ac_score += error_score[charachters[idx]]
            ac_scores.append(line_ac_score)


print(sorted(ac_scores)[len(ac_scores) // 2])
