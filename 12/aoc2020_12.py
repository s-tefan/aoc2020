def mmult(A,B):
    '''Multiply matrix A with vector B.'''
    return tuple(sum([a[j]*x for j,x in enumerate(B)]) for a in A)
    

class Boat:
    dirs  = {'S':(0,-1), 'N':(0,1), 'E':(1,0), 'W':(-1,0)}
    turns = {('L',90):((0,-1),(1,0)), ('R',90):((0,1),(-1,0)), ('L',180):((-1,0),(0,-1)), ('R',180):((-1,0),(0,-1)),
        ('R',270):((0,-1),(1,0)), ('L',270):((0,1),(-1,0))}
    ahead  = {'F'}

    def __init__(self):
        self.position = [0,0]
        self.direction = self.dirs['E']

    def __str__(self):
        return 'Boat in position: {}, direction: {})'.format(self.position, self.direction)
    
    def read(self, f):
        lines = [line.strip() for line in f]
        self.instructions = [(line[0], int(line[1:])) for line in lines]
    
    def do(self, instr):
        comm = instr[0]
        if comm in self.dirs:
            self.position = map(lambda p, d: p + instr[1]*d, self.position, self.dirs[comm])
        elif instr in self.turns:
            self.direction = mmult(self.turns[instr], self.direction)
        elif comm in self.ahead:
            self.position = tuple(p + instr[1]*self.direction[j] for j,p in enumerate(self.position))
        else:
            raise Exception('Unknown boat navigation command', instr)
    
    def navigate(self):
        for instr in self.instructions:
            self.do(instr)

    def manhattan(self):
        return abs(self.position[0])+abs(self.position[1])


b = Boat()
with open("input.txt") as f:
    b.read(f)
print(b)
b.navigate()
print(b)
print(b.manhattan())

