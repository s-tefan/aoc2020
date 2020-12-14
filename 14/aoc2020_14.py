class Aoc14:
    def __init__(self):
        self.codelist = []
        self.count = 0
        self.mem = {}

    def read(self, filename):
        with open(filename) as f:
            for line in f:
                a, b = line.strip().split("=")
                self.codelist.append((a.strip(), b.strip()))

    def run_single(self):
        comm = self.codelist[self.count]
        if comm[0] == "mask":
            self.setmask(comm[1])
        elif comm[0][:3] == "mem":
            s = comm[0]
            addr = int(s[s.find("[")+1:s.find("]")])
            val = int(comm[1])
            self.setmem(addr, val)
    
    def run(self):
        for k, line in enumerate(self.codelist):
            self.count = k
            self.run_single()
        
    def setmask(self, s):
        self.ormask = int(s.replace("X", "0"), 2)
        self.andmask = int(s.replace("X", "1"), 2)

    def setmem(self, addr, val):
        self.mem[addr] = val & self.andmask | self.ormask

    def memsum(self):
        return sum(self.mem[k] for k in self.mem if self.mem[k] != 0)

blubb = Aoc14()
blubb.read("input.txt")
blubb.run()
print(blubb.memsum())
