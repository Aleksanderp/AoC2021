# This is a disaster but i am too tired

from math import ceil as roundup


class Pair:
    def __init__(self):
        self.branches = [None, 0] # pylance idk
        self.parent = None
        return
    
    @staticmethod
    def decode(line, parent):
        if len(line) == 1:
            return int(line[0])

        commaIdx = Pair.findcomma(line)
        if commaIdx == None:
            return None
        p = Pair()
        p.parent = parent
        p.branches[0] = Pair.decode(line[1:commaIdx], p)
        p.branches[1] = Pair.decode(line[commaIdx +1:-1], p)
        return p
        
    @staticmethod
    def findcomma(line):
        nested = 0
        for idx in range(len(line)):
            if line[idx] == "[":
                nested += 1
            elif line[idx] == "]":
                nested -= 1
            
            if line[idx] == "," and nested == 1:
                return idx
        return None
    
    def add(self, right):
        p = Pair()
        p.parent = None
        p.branches[0] = self
        p.branches[1] = right

        self.parent = p
        right.parent = p
        return p

    def reduce(self):
        r = self.explode(1)
        if r != None and r.parent != None:
            for i in range(2):
                if r.parent.branches[i] == r:
                    other = (i +1) % 2
                    # node where we are not on the i side
                    node = r.parent.notAnIBranch(r, i)
                    if node != None:
                        node.addToISide(i, r.branches[i])
                    r.parent.addToISide(other, r.branches[other])
                    r.parent.branches[i] = 0
                    break
            return 0
        return self.split()

    def explode(self, depth):
        for i in range(0, 2):
            if isinstance(self.branches[i], Pair):
                r = self.branches[i].explode(depth +1)
                if r != None:
                    return r
        if depth >= 5:
            return self
        return None

    def addToISide(self, i, ammount):
        other = (i +1) % 2
        if isinstance(self.branches[i], int):
            self.branches[i] += ammount
        else:
            self.branches[i].mostISideAdd(other, ammount)

    def notAnIBranch(self, iChild, i):
        if self.branches[i] != iChild:
            return self
        if self.parent == None:
            return None
        return self.parent.notAnIBranch(self, i)

    def mostISideAdd(self, priority, ammount):
        other = (priority +1) % 2
        for i in [priority, other]:
            if isinstance(self.branches[i], int):
                self.branches[i] += ammount
                return 0
            r = self.branches[i].mostISideAdd(priority, ammount)
            if r != None:
                return r
        return None
            
    def split(self):
        for i in range(0, 2):
            if isinstance(self.branches[i], int) and self.branches[i] >= 10:
                p = Pair()
                p.parent = self
                p.branches[0] = self.branches[i] // 2
                p.branches[1] = roundup(self.branches[i] / 2)
                self.branches[i] = p
                return 0
            
            if isinstance(self.branches[i], Pair):
                r = self.branches[i].split()
                if r != None:
                    return r
        return None

    def magnitude(self):
        result = 0
        if isinstance(self.branches[0], int):
            result += 3 * self.branches[0]
        else:
            result += 3 * self.branches[0].magnitude()

        if isinstance(self.branches[1], int): 
            result += 2 * self.branches[1]
        else:
            result += 2 * self.branches[1].magnitude()
        return result

    def print(self):
        self.rprint()
        print("")

    def rprint(self):
        print("[", end="")
        for i in range(0, 2):
            if isinstance(self.branches[i], int):
                print(self.branches[i], end="")
            else:
                self.branches[i].rprint()
            if i == 0:
                print(",", end="")
        print("]", end="")

pairs = []
source = []
with open("day18.txt", "r") as dat:
    for line in dat:
        stripped = list(line.strip("\n\r"))
        p = Pair.decode(stripped, None)
        source.append(stripped)
        pairs.append(p)

# =============== [ PART 1 ] =============== #
print("PART 1:")
all_summed = pairs[0]
for i in range(1, len(pairs)):
    all_summed = all_summed.add(pairs[i])
    while all_summed.reduce() != None: pass
all_summed.print()
print(all_summed.magnitude())

# =============== [ PART 2 ] =============== #
# Super slow due to constant decoding but i will maybe fix that later for now this works :D
print("PART 2")
max_magnitude = 0
for i in range(0, len(source)):
    for j in range(0, len(source)):
        if i == j:
            continue
        pi = Pair.decode(source[i], None)
        pj = Pair.decode(source[j], None)
        # pylance
        if not isinstance(pi, Pair) or not isinstance(pj, Pair):
            continue
        summed = pi.add(pj )
        while summed.reduce() != None: pass
        mag = summed.magnitude()
        if  mag > max_magnitude:
            max_magnitude = mag
print(max_magnitude)
