def count_greater_n_sums(arr, size):
    running_sum = [arr[0]]
    equal = 0
    for i in range(1, len(arr)):
        running_sum.append(running_sum[i-1] + arr[i])
        if i < size:
            continue
        sum_two = running_sum[i] - running_sum[i - size]
        sum_one = running_sum[i -1] - running_sum[max(i - size - 1,0)]
        if sum_one < sum_two:
                equal +=1
    return equal

values = []
with open("day1.txt", "r") as dat:
    for line in dat:
        values.append(int(line))

print(count_greater_n_sums(values, 1))
print(count_greater_n_sums(values, 3))
