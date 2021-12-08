def ordered_segment(segment):
    return "".join(sorted(list(segment)))

def add_segment(number_to_segments, segment, numbers):
    for n in numbers:
        number_to_segments[n] = number_to_segments.setdefault(n, "") + segment

def ordered_segments_to_numbers(number_to_segments):
    segments_to_numbers = {}
    for number in number_to_segments.keys():
        ord_segment = ordered_segment(number_to_segments[number])
        segments_to_numbers[ord_segment] = number
    return segments_to_numbers

numbers_by_length = {2: 1, 4:4, 3:7, 7:8}
total = 0
with open("day8_2.txt", "r") as dat:
    for line in dat:
        splitted = line.split(" | ")
        inputd = splitted[0]
        output = splitted[1].strip("\n\r ")
        
        number_to_segments = {}
        segments_counts = {}
        for digit in inputd.split(" "):
            digit_len = len(digit)
            if numbers_by_length.get(digit_len) is not None:
                num = numbers_by_length[digit_len]
                number_to_segments[num] = digit
            for d in digit:
                segments_counts[d] = 1+ segments_counts.setdefault(d, 0)
        top = ""
        # get top right_top right_bottom
        for d in number_to_segments[7]:
            if d not in number_to_segments[1]:
                top = d
                add_segment(number_to_segments, d, [0, 2, 3, 5, 6, 9])
            elif segments_counts[d] == 8:
                add_segment(number_to_segments, d, [0, 2, 3, 9])
            elif segments_counts[d] == 9:
                add_segment(number_to_segments, d, [0, 3, 5, 6, 9])
        
        # get left_top and middle
        for d in number_to_segments[4]:
            if d not in number_to_segments[1]:
                if segments_counts[d] == 6:
                    add_segment(number_to_segments, d, [0, 5, 6, 9])
                if segments_counts[d] == 7:
                    add_segment(number_to_segments, d, [2, 3, 5, 6, 9])
        
        # bottom and left_bottom
        for d in number_to_segments[8]:
            if d not in number_to_segments[4] and d != top:
                if segments_counts[d] == 4:
                    add_segment(number_to_segments, d, [0, 2, 6])
                if segments_counts[d] == 7:
                    add_segment(number_to_segments, d, [0, 2, 3, 5, 6, 9])

        segment_to_number = ordered_segments_to_numbers(number_to_segments)
        number = 0
        for num in output.split(" "):
            number *= 10
            number += segment_to_number[ordered_segment(num)]
        total += number
print(total)
