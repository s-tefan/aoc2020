""" Advent of Code 2020, day 17."""
__author__ = "Stefan Karlsson"
__date__ = "2020-12-17"

class ConwayCubes:
    """A class for the 3D version of Conways Game of Life."""
    def __init__(self, file = None):
        if file:
            self.active_set = set()
            for x, line in enumerate(file):
                for y, c in enumerate(line.strip()):
                    if c == '#':
                        self.activate((x,y,0))
        else:
            self.active_set = {(0,1,0), (1,2,0), (2,0,0), (2,1,0), (2,2,0)}

    def __str__(self):
        s = ''
        xvalues = [p[0] for p in self.active_set]
        yvalues = [p[1] for p in self.active_set]
        zvalues = [p[2] for p in self.active_set]
        for z in range (min(zvalues),max(zvalues)+1):
            s += 'z={}\n'.format(z)
            for x in range (min(xvalues),max(xvalues)+1):
                for y in range (min(yvalues),max(yvalues)+1):
                    s += '#' if self.is_active((x,y,z)) else '.'
                s += '\n'
        return s

    def activenumber(self):
        """Return the number of active cells in the grid."""
        return len(self.active_set)

    def neighbourhood(self, pos):
        """A generator for the neighbours of a cell in a 3D grid."""
        r = range(-1, 2)
        for dx in r:
            for dy in r:
                for dz in r:
                    if (dx,dy,dz) == (0,0,0):
                        pass
                    else:
                        yield tuple(map(sum, zip(pos,(dx, dy, dz))))

    def is_active(self, pos):
        """Check if cell at pos is active."""
        return k in self.active_set

    def activate(self, pos):
        """Activate cell at pos."""
        self.active_set.add(pos)

    def inactivate(self, pos):
        """Inactivate cell at po."""
        self.active_set.discard(pos)

    def update(self):
        """Update the grid."""
        neighbourcount_dict = {}
        for pos in self.active_set:
            if pos not in neighbourcount_dict:
                neighbourcount_dict[pos] = 0
            for k in self.neighbourhood(pos):
                if k in neighbourcount_dict:
                    neighbourcount_dict[k] += 1
                else:
                    neighbourcount_dict[k] = 1
        for (pos, count) in neighbourcount_dict.items():
            if self.is_active(pos):
                if count not in {2,3}:
                    self.inactivate(pos)
            else:
                if count == 3:
                    self.activate(pos)

class ConwayHyperCubes(ConwayCubes):
    """Modification of ConwayCubes for 4D."""
    def __init__(self, file = None):
        if file:
            self.active_set = set()
            for x, line in enumerate(file):
                for y, c in enumerate(line.strip()):
                    if c == '#':
                        self.activate((x,y,0,0))
        else:
            self.active_set = {(0,1,0,0), (1,2,0,0), (2,0,0,0), (2,1,0,0), (2,2,0,0)}

    def __str__(self):
        s = ''
        xvalues = [p[0] for p in self.active_set]
        yvalues = [p[1] for p in self.active_set]
        zvalues = [p[2] for p in self.active_set]
        wvalues = [p[3] for p in self.active_set]
        for w in range (min(wvalues),max(wvalues)+1):
            for z in range (min(zvalues),max(zvalues)+1):
                s += 'z={}, w={}\n'.format(z,w)
                for x in range (min(xvalues),max(xvalues)+1):
                    for y in range (min(yvalues),max(yvalues)+1):
                        s += '#' if self.is_active((x,y,z,w)) else '.'
                    s += '\n'
        return s

    def neighbourhood(self, pos):
        """A generator for the neighbours of a cell in a 4D grid."""
        r = range(-1, 2)
        for dx in r:
            for dy in r:
                for dz in r:
                    for dw in r:
                        if (dx,dy,dz,dw) == (0,0,0,0):
                            pass
                        else:
                            yield tuple(map(sum, zip(pos,(dx, dy, dz, dw))))

"""Class definitions over. Test programs and problem run follows."""

def partone():
    """Run the test case for part one."""
    with open("input.txt") as f:
        grid = ConwayCubes(f)
        for k in range(6):
            grid.update()
        return grid.activenumber()

def parttwo():
    """Run the test case for part two."""
    with open("input.txt") as f:
        grid = ConwayHyperCubes(f)
        for k in range(6):
            grid.update()
        return grid.activenumber()

def testone():
    """Run part one of AoC 2020 day 17."""
    grid = ConwayCubes()
    print(grid)
    for k in range(6):
        grid.update()
        print("After {} cycles".format(k+1))
        print("{} active cubes".format(grid.activenumber()))
        print(grid)
    print(len(list(filter(lambda x: x=="#",grid.__str__()))))
    return grid.activenumber()

def testtwo(cycles = 6, verbose = False):
    """Run part two of AoC 2020 day 17."""
    grid = ConwayHyperCubes()
    if verbose:
        print(grid)
    for k in range(cycles):
        grid.update()
        if verbose:
            print("After {} cycles".format(k+1))
            print("{} active cubes".format(grid.activenumber()))
            print(grid)
    return grid.activenumber()

#print(testone())
#print(testtwo())

"""Run and time part one and part two."""
import time
tstack=[]
#Part one
tstack.append(time.process_time())
print('Part one: {}'.format(partone()))
tstack.append(time.process_time())
print("Time: {}".format(tstack.pop()-tstack.pop()))
#Part two
tstack.append(time.process_time())
print('Part two: {}'.format(parttwo()))
tstack.append(time.process_time())
print("Time: {}".format(tstack.pop()-tstack.pop()))
