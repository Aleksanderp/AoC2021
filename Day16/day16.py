# Part 2 functions
class Functions:
    def sum(self, a, b):        return a + b
    def product(self, a, b):    return a * b
    def min(self, a, b):        return a if a < b else b
    def max(self, a, b):        return a if a > b else b
    def greater(self, a, b):    return int(a > b)
    def lesser(self, a, b):     return int(a < b)
    def equal(self, a, b):      return int(a == b)
    def __getitem__(self, name):
        return getattr(self, name)
f = Functions()
functions = {
    0: "sum",
    1: "product",
    2: "min",
    3: "max",
    5: "greater",
    6: "lesser",
    7: "equal"
}

# Read hex into bin with leading 0
with open("day16.txt", "r") as dat:
    data = dat.readline().strip("\n\r")
    binary = bin(int(data, 16))[2:].zfill(len(data) * 4)

def add(idx, length, result):
    # convert to int starting with result
    for i in range(0, length):
        result *= 2
        if binary[idx + i] == '1':
            result += 1
    return (idx + length, result)

def read_literal(idx):
    number = 0
    # sum all groups starting with one
    while binary[idx] == '1':
        idx, number = add(idx+1, 4, number)
    # add final group
    return add(idx + 1, 4, number)
    
version_sum = 0
def read_packet(idx):
    # Part 1
    global version_sum
    idx, version = add(idx, 3, 0)
    version_sum += version

    # Type
    idx, type = add(idx, 3, 0)
    
    # Literal
    if type == 4:   
        idx, literal = read_literal(idx)
        return (idx, literal)

    # Length ID
    idx, lengthID = add(idx, 1, 0)

    # Read by length
    if lengthID == 0:
        idx, length = add(idx, 15, 0)
        end = idx + length 
        idx, result = read_packet(idx)
        while idx < end:
            idx, value = read_packet(idx)
            result = f[functions[type]](result, value)
        return idx, result

    # Read by packets
    idx, packetsCount = add(idx, 11, 0)
    idx, result = read_packet(idx)
    for _ in range(packetsCount-1):
        idx, value = read_packet(idx)
        result = f[functions[type]](result, value)
    return idx, result

# read all packets (starting idx = 0)
_, value = read_packet(0)
print("Part_1:", version_sum)
print("Part_2:", value)
