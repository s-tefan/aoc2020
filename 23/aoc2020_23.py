class Crabgame:
    def __init__(self, startlist, ringsize, startlast, startnext, last):
        self.startlist = startlist
        self.succdict = {}
        self.ringsize = ringsize
        for j, k in enumerate(startlist[:-1]):
            self.succdict[k] = startlist[j+1]
        self.succdict[last] = startlist[0]
        self.succdict[startlast] = startnext
        self.current = self.startlist[0]

    def __iter__(self):
        self.current = self.startlist[0]
        return self

    def succ(self, n):
        return self.succdict.get(n, (n % self.ringsize) + 1)

    def oneless(self, n):
        return ((n - 2) % self.ringsize) + 1

    def dest(self):
        k = self.current - 1
        while k in self.pickuplist():
            k -= 1
        return k

    def __next__(self):
        dest = self.oneless(self.current)
        pickup = self.current
        pickupset = set()
        for k in range(3):
            pickup = self.succ(pickup)
            pickupset.add(pickup)
        while dest in pickupset:
            dest = self.oneless(dest)
        ds = self.succ(dest)
        ps = self.succ(pickup)
        self.succdict[dest] = self.succ(self.current)
        self.succdict[pickup] = ds
        self.succdict[self.current] = ps
        self.current = self.succ(self.current)
        return self


def run(game, n, verbose=False, partone=False, parttwo=False):
    p = game.current
    if verbose:
        print("Start:")
        for a in range(len(game.succdict)):
            print('{}, '.format(p), end='')
            p = game.succ(p)
            print()
    for j in range(n):
        next(game)
        if verbose:
            print("After {} moves:".format(j+1))
            print(game.current, game.succdict)
            p = game.current
            for a in range(len(game.succdict)):
                print('{}, '.format(p), end='')
                p = game.succ(p)

    if partone:
        p = 1
        s = ''
        for k in range(8):
            p = game.succ(p)
            s += (str(p))
        print(s)
    if parttwo:
        p = game.succ(1)
        q = game.succ(p)
        print("{} * {} = {}".format(p, q, p*q))


def start():
    test = Crabgame(
        startlist=[3, 8,  9,  1,  2,  5,  4,  6,  7],
        ringsize=9,
        startlast=7,
        startnext=3,
        last=7)
    #run(test, 100)

    mystartlist = [int(c) for c in "389547612"]
    partonegame = Crabgame(
        startlist=mystartlist,
        ringsize=len(mystartlist),
        startlast=mystartlist[-1],
        startnext=mystartlist[0],
        last=mystartlist[-1])
    run(partonegame, 100, verbose=False, partone=True, parttwo=False)

    test2 = Crabgame(
        startlist=[3, 8,  9,  1,  2,  5,  4,  6,  7],
        ringsize=10 ** 6,
        startlast=7,
        startnext=10,
        last=10 ** 6)
    #run(test2, 10 ** 7, verbose = False, partone = True, parttwo = True)

    parttwogame = Crabgame(
        startlist=mystartlist,
        ringsize=10 ** 6,
        startlast=mystartlist[-1],
        startnext=10,
        last=10 ** 6)
    run(parttwogame, 10 ** 7, verbose=False, partone=False, parttwo=True)


start()
