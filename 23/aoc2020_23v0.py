class Cup:
    min = None
    max = None
    last = None
    start = None
    def __init__(self, label, next = None):
        self.label = label
        self.next = next
        Cup.start = self
    def __init__(self, maxlabel = None, labellist = None):
        if labellist:
            # här behövs fixas till!
            mini = min(labellist)
            maxi = max(labellist)
            Cup.min, Cup.max = mini, maxi
            Cup.start = self
            follow = self
            Cup.last = Cup()
            Cup.last.label = maxi
            Cup.last.next = self
            follow = Cup.last
            for label in reversed(labellist[1:-1]):
                cup = Cup()
                cup.label = label
                cup.next = follow
                follow = cup
            self.label = labellist[0]
            self.next = follow
        else:
            self.next = None
        
    def pickup3(self):
        p = self.next
        self.next = self.next.next.next.next
        return p
    def insert3(self, ins):
        ins.next.next.next = self.next
        self.next = ins
    def labelset(self,n):
        if n <= 0:
            return set()
        else:
            a = self.next.labelset(n-1)
            a.add(self.label)
            return a
    # def findlabel(self, label):
    #     if self.label == label:
    #         return self
    #     elif label in range(Cup.min, Cup.max + 1):
    #         return self.next.findlabel(label)
    #     else:
    #         return None
    def findlabel(self, label):
        if label in range(Cup.min, Cup.max + 1):
            test = Cup.start
            while test.label != label:
                test = test.next
            return test
        else:
            return None

    def destination(self, pick):
        picklabels = pick.labelset(3)
        n = self.label -1
        while n in picklabels:
            n -= 1
        if n < Cup.min:
            n = Cup.max
            Cup.last.insert3(pick)
            Cup.start = pick
            return Cup.last
        else:
            return self.findlabel(n)
        # Kan bli fel på slutet när Cup.last hamnar i pickups, om inte Cup.last uppdateras
        
    def move(self):
        pick = self.pickup3()
        dest = self.destination(pick)
        dest.insert3(pick)
        return self.next
    

def partone():
    test = Cup([3, 8,  9,  1,  2,  5,  4,  6,  7])
    #apa = Cup([int(a) for a in list("389547612")])
    apa = test
    print(Cup.last.label, Cup.last.next.label, Cup.start.label)
    for n in range(100):
        bepa = apa.move()
        apa = bepa
        print("After move {}: . current: {}, start: {}, last: {}".format(n+1, apa.label, Cup.start.label, Cup.last.label), end="\t")
        for k in range(9):
            print(bepa.label, end="")
            bepa = bepa.next
        print()
        apa = bepa

    bepa = apa.findlabel(1).next
    for k in range(8):
        print(bepa.label, end="")
        bepa = bepa.next
    print()

def parttwo(input):
    current = Cup([int(a) for a in list(input)] + list(range(len(input)+1, 1000000 +1)))
    for n in range(10000):
        if not n%100: print(n)
        # blupp = Cup.start
        # for k in range(100):
        #     print(blupp.label, end=" ")
        #     if blupp == current: print(".", end="") 
        #     blupp = blupp.next
        # print()
        current = current.move()
    bepa = current.findlabel(1)
    return bepa.next.label * bepa.next.next.label 

partone()
#print(parttwo("389547612"))