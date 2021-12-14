# Part 1: STEPS = 10
# Part 2: STEPS = 40
STEPS = 1000

with open("day14.txt", "r") as dat:
    polymer = list(dat.readline().strip("\n\r"))
    firs_element = polymer[0]
    dat.readline()

    substitutions = {}
    for line in dat:
        pair, addition = line.strip("\n\r").split(" -> ")
        substitutions[pair] = addition
    valid_pairs = substitutions.keys()

    elements_count = {firs_element: 1}
    element_pairs = {}
    for i in range(1, len(polymer)):
        pair=polymer[i-1] + polymer[i]
        elements_count[polymer[i]] = elements_count.get(polymer[i], 0) +1
        if pair not in valid_pairs:
            continue
        element_pairs[pair] = element_pairs.get(pair, 0) +1

def changeCount(counts, pair, count):
    if pair not in valid_pairs:
        return
    counts[pair] = counts.get(pair, 0) + count

for _ in range(STEPS):
    new_pairs = {}
    for pair, count in element_pairs.items():
        new_element = substitutions[pair]
        elements_count[new_element] = elements_count.get(new_element, 0) +count
        first_pair = pair[0] + new_element
        second_pair = new_element + pair[1]
        changeCount(new_pairs, first_pair, count)
        changeCount(new_pairs, second_pair, count)
    element_pairs = new_pairs

most_common = elements_count[firs_element]
least_common = elements_count[firs_element]
for val in elements_count.values():
    if val > most_common:
        most_common = val
    if val < least_common:
        least_common = val
print(most_common - least_common)
