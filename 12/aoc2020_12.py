def mmult(A,B):
    '''Multiply matrix A with vector B.'''
    return tuple(sum([a[j]*x for j,x in enumerate(B)]) for a in A)

def vsum(A,B):
    return tuple(map(sum, zip(A,B)))

def vmult(A, k):
    return tuple(k*a for a in A)
    

class Boat:
    dirs  = {'S':(0,-1), 'N':(0,1), 'E':(1,0), 'W':(-1,0)}
    turns = {('L',90):((0,-1),(1,0)), ('R',90):((0,1),(-1,0)), ('L',180):((-1,0),(0,-1)), ('R',180):((-1,0),(0,-1)),
        ('R',270):((0,-1),(1,0)), ('L',270):((0,1),(-1,0))}
    ahead  = {'F'}

    def __init__(self, position = (0,0), direction = (1,0), wp = False):
        self.position = position
        self.direction = direction
        self.wp = wp

    def __str__(self):
        return 'Boat in position: {}, direction: {}, using wp: {})'.format(self.position, self.direction, self.wp)
    
    def read(self, f):
        lines = [line.strip() for line in f]
        self.instructions = [(line[0], int(line[1:])) for line in lines]
    
    def do(self, instr):
        comm = instr[0]
        if comm in self.dirs:
            if self.wp:
                self.direction = vsum(self.direction, vmult(self.dirs[comm], instr[1]))
            else:
                self.position = vsum(self.position, vmult(self.dirs[comm], instr[1]))
        elif instr in self.turns:
            self.direction = mmult(self.turns[instr], self.direction)
        elif comm in self.ahead:
            self.position = vsum(self.position, vmult(self.direction, instr[1]))
        else:
            raise Exception('Unknown boat navigation command', instr)
        #print(b)
    
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

b = Boat(direction = (10,1), wp = True)
with open("input.txt") as f:
    b.read(f)
print(b)
b.navigate()
print(b)
print(b.manhattan())

