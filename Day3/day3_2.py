numbers = []
with open("day3_2.txt", "r") as dat:
    for line in dat:
        stripped = line.strip("\n\r")
        numbers.append(stripped)

def is_one_most_common(numbers, idx):
    ones = 0
    for i in numbers:
        if i[idx] == "1":
            ones += 1
        if ones >= len(numbers) / 2:
            return True
    return False

def remove_invalid(numbers, idx, correct):
    result = []
    for num in numbers:
        if num[idx] == correct:
            result.append(num)
    return result

def read_value(numbers, default_keep, if_keep):
    idx = 0
    while (len(numbers) > 1):
        keep = default_keep
        if is_one_most_common(numbers, idx):
            keep = if_keep
        numbers = remove_invalid(numbers, idx, keep)
        idx += 1
    return int(numbers[0], 2)

oxygen_generator_rating = read_value(numbers, "0", "1")
co2_scrubber_rating = read_value(numbers, "1", "0")

print(oxygen_generator_rating * co2_scrubber_rating)
