from functools import reduce

def xeuclid(a, b):
    r = a % b
    q = a // b
    if r == 0:
        return b, 1, q-1
    else:
        g, x, y = xeuclid(b, r)
        return g, (-y) % b, (-x - q*y) % a

def partone():
    with open("input.txt") as f:
        departure = int(f.readline().strip())
        busids = list(map( lambda x: int(x), (filter(lambda x: x != 'x', map(lambda x: x.strip(), f.readline().split(','))))))
    minimal = {}
    for id in busids:
        t = -departure % id
        if not minimal or t < minimal['t']:
            minimal = {'id': id, 't': t }
    return (minimal['id']*minimal['t'])

def parttwo():
    with open("input.txt") as f:
        departure = int(f.readline().strip())
        strlist = map(lambda x: x.strip(), f.readline().split(','))
        buslist = list(map(lambda x: (x[0], int(x[1])), filter(lambda x: x[1]!='x', enumerate(strlist))))
        # Check coprimality
        mlist = [bus[1] for bus in buslist]
        for i, a in enumerate(mlist):
            for b in mlist[:i]:
                d, _, _ = xeuclid(a,b)
                if d != 1: raise Exception("Not coprime") 
        # Chinese remainder solving
        N = reduce(lambda x1, x2: x1*x2[1], buslist, 1)
        x = 0
        for k, bus in enumerate(buslist):
            a, m = bus
            d, x1, _ = xeuclid(N//m, m)
            x += x1*(-a)*N//m
            x = x % N
        # print([(x+bus[0]) % bus[1] for bus in buslist]) # Check correct solution
        return(x)
        
print(partone(), parttwo())
