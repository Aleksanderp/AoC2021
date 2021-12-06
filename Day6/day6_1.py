DAYS = 80

fish = []
with open("day6_1.txt", "r") as dat:
    fish = [int(x) for x in dat.readline().split(",")]

for d in range(DAYS):
    new_fish = []
    for idx in range(len(fish)):
        if fish[idx] == 0:
            new_fish.append(8)
            fish[idx] = 7
        fish[idx] -= 1
    fish += new_fish

print(len(fish))
