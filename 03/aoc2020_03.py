def one(filename):
    with open(filename) as f:
        treecount = 0
        right = 0
        down = 0
        while True:
            inputline = f.readline().strip("\n")
            if not inputline: 
                break
            else:
                if inputline[right] == '#':
                    treecount += 1
                    #print( inputline[:right]+"X"+inputline[right+1:])
                #else:
                    #print( inputline[:right]+"O"+inputline[right+1:])
                #print(inputline)
                down += 1
                right = (right + 3) % len(inputline)
    return treecount


def two(filename):
    with open(filename) as f:
        runs = ((1,1),(3,1),(5,1),(7,1),(1,2))
        pos = [0]*len(runs)
        treecounts = [0]*len(runs)
        down = 0
        while True:
            inputline = f.readline().strip("\n")
            if not inputline: 
                break
            else:
                for (j,run) in enumerate(runs):
                    if not down % run[1]:
                        if inputline[pos[j]] == '#':
                            treecounts[j] += 1
                            #print( inputline[:pos[j]]+"X"+inputline[pos[j]+1:])
                        else:
                            pass #print( inputline[:pos[j]]+"O"+inputline[pos[j]+1:])
                        pos[j] = (pos[j] + run[0]) % len(inputline)
                    else: 
                        pass #print(inputline)
                    
                down += 1
        return treecounts

print( one("input.txt"))
treecounts = two("input.txt")
p=1
for c in treecounts:
    p *= c
print(p, treecounts)

