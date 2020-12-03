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

print( one("input.txt"))

