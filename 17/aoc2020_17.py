def gridval_to_str(grid):
        s = ''
        xvalues = [p[0] for p in grid]
        yvalues = [p[1] for p in grid]
        zvalues = [p[2] for p in grid]
        for z in range (min(zvalues),max(zvalues)+1):
            s += 'z={}\n'.format(z)
            for x in range (min(xvalues),max(xvalues)+1):
                for y in range (min(yvalues),max(yvalues)+1):
                    s += str(grid[(x,y,z)]) if (x,y,z) in grid else '.'
                s += '\n'
        return s


class ConwayCubes:
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
        return len(self.active_set)

    '''
    def activecount(self, r):
        return sum(self.is_active(k) for k in r)
    '''

    def neighbourhood(self, pos):
        r = range(-1, 2)
        for dx in r:
            for dy in r:
                for dz in r:
                    if (dx,dy,dz) == (0,0,0):
                        pass
                    else:
                        yield tuple(map(sum, zip(pos,(dx, dy, dz))))

    def is_active(self,k):
        return k in self.active_set

    def activate(self,pos):
        self.active_set.add(pos)

    def inactivate(self,pos):
        self.active_set.discard(pos)


    def update(self):
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
        print(gridval_to_str(neighbourcount_dict))
        
def partone():
    with open("input.txt") as f:
        grid = ConwayCubes(f)
        for k in range(6):
            grid.update()
        return grid.activenumber()

def testone():
    grid = ConwayCubes()
    print(grid)
    for k in range(6):
        grid.update()
        print("After {} cycles".format(k+1))
        print("{} active cubes".format(grid.activenumber()))
        print(grid)
    print(len(list(filter(lambda x: x=="#",grid.__str__()))))
    return grid.activenumber()

#print(testone())
import time
tstack=[]
tstack.append(time.process_time())
print(partone())
tstack.append(time.process_time())
print("Time: {}".format(tstack.pop()-tstack.pop()))

