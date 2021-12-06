DAYS = 256

fish = {}
total = 0
with open("day6_2.txt", "r") as dat:
    for f in dat.readline().split(","):
        fish[int(f)] = 1 + fish.setdefault(int(f), 0)
        total += 1

for d in range(DAYS):
    current = fish.setdefault(d, 0)
    fish[d + 7] = fish.setdefault(d + 7, 0) + current
    fish[d + 9] = fish.setdefault(d + 9, 0) + current
    total += current
print(total)
