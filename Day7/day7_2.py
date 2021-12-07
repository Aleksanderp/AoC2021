def calculate_cost(pos, pos_two):
    n = abs(pos - pos_two)
    return (n) * (n +1) // 2
    
fuel_cost = {}
minimal = None
with open("day7_2.txt", "r") as dat:
    positions = list(map(int, dat.readline().split(",")))
    for pos in range(min(positions), max(positions) +1):
        fuel_cost[pos] = 0
        for pos_two in positions:
            fuel_cost[pos] += calculate_cost(pos, pos_two)
        if minimal is None or fuel_cost[pos] < minimal:
            minimal = fuel_cost[pos]
print(minimal)
