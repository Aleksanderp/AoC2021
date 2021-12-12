class Cave:
    def __init__(self, code):
        self.exits = []
        self.code = code
        self.visits = 0
        self.isSmall = self.code.islower()
    
    def add_exit(self, exit):
        self.exits.append(exit)

    def paths_to_end(self, visitTwice):
        if self.code == "end":
            # cave should be visited twice
            if visitTwice != None and caves[visitTwice].visits != 2:
                return 0
            return 1
        # other caves can only be visited once
        if self.code != visitTwice and self.isSmall and self.visits == 1:
            return 0
        
        # one cave can be visited twice
        if self.code == visitTwice and self.visits == 2:
            return 0

        self.visits += 1
        paths = 0
        for c in self.exits:
            paths += c.paths_to_end(visitTwice)
        self.visits -= 1
        return paths
        

caves = {}
small_caves = set()
with open("day12.txt", "r") as dat:
    for path in dat:
        start, end = path.strip("\n\r").split("-")
        if start.islower():
            small_caves.add(start)
        if end.islower():
            small_caves.add(end)
        if caves.get(start) == None:
            caves[start] = Cave(start)
        if caves.get(end) == None:
            caves[end] = Cave(end)
        caves[start].add_exit(caves[end])
        caves[end].add_exit(caves[start])
small_caves.remove("start")
small_caves.remove("end")

# specify a cave to visit twice and count paths
paths = caves["start"].paths_to_end(None)
print("Part 1:", paths)
for c in small_caves:
    paths += caves["start"].paths_to_end(c)
print("Part 2:", paths)
