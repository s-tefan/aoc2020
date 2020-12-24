class Hextile:
    dircoords = {'w': (-1, 0), 'e': (1, 0), 'sw': (0, -1),
                 'se': (1, -1), 'nw': (-1, 1), 'ne': (0, 1)}
    blacklist = set()

    def __init__(self):
        self.coords = (0, 0)

    def moveflip(self, dirstring):
        while dirstring:
            if dirstring[0] in {'n', 's'}:
                d = Hextile.dircoords[dirstring[:2]]
                dirstring = dirstring[2:]
            elif dirstring[0] in {'w', 'e'}:
                d = Hextile.dircoords[dirstring[:1]]
                dirstring = dirstring[1:]
            else:
                raise Error("Wrong character")
            self.coords = self.coords[0] + d[0], self.coords[1] + d[1]
        Hextile.blacklist = Hextile.blacklist.symmetric_difference({
                                                                   self.coords})
    @classmethod
    def neighbours(cls):
        neighbourdict = {}
        for c in cls.blacklist:
            for d in cls.dircoords.values():
                e = (c[0]+d[0],c[1]+d[1])
                if e in neighbourdict.keys():
                    neighbourdict[e] += 1
                else:
                    neighbourdict[e] = 1
        blackflip = cls.blacklist.difference(neighbourdict.keys()).\
            union({a for (a,b) in neighbourdict.items() if (b > 2)})
        whiteflip =  {a for (a,b) in neighbourdict.items() if b == 2 and a not in cls.blacklist}
        cls.blacklist = cls.blacklist.difference(blackflip).union(whiteflip)

    @classmethod
    def reset(cls):
        cls.blacklist = set()

def partone(filename):
    with open(filename) as f:
        for line in f:
            Hextile().moveflip(line.strip('\n'))
    return len(Hextile.blacklist)

def parttwo(filename, verbose = False):
    Hextile.reset()
    partone(filename)
    for k in range(100):
        Hextile.neighbours()
        if verbose: print('Day {}: {}', k+1, len(Hextile.blacklist) )
    return len(Hextile.blacklist)

print(partone("input.txt"))
print(parttwo("input.txt"))