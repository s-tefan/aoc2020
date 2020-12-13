from functools import reduce

def xeuclid(a, b):
    '''Extended euclidian algorithm: Solve a*x == b*y + g, g = gcd(a,b). Yields smallest non-negative solution.'''
    r = a % b
    q = a // b
    if r == 0:
        return b, 1, q-1
    else:
        g, x, y = xeuclid(b, r)
        return g, (-y) % b, (-x - q*y) % a

def partone(filename):
    with open(filename) as f:
        departure = int(f.readline().strip())
        busids = list(map( lambda x: int(x), (filter(lambda x: x != 'x', map(lambda x: x.strip(), f.readline().split(','))))))
    minimal = {}
    for id in busids:
        t = -departure % id
        if not minimal or t < minimal['t']:
            minimal = {'id': id, 't': t }
    return (minimal['id']*minimal['t'])

def parttwo(filename):
    with open(filename) as f:
        departure = int(f.readline().strip())
        strlist = map(lambda x: x.strip(), f.readline().split(','))
        buslist = list(map(lambda x: (x[0], int(x[1])), filter(lambda x: x[1]!='x', enumerate(strlist))))
        # Check coprimality
        mlist = [bus[1] for bus in buslist]
        for i, a in enumerate(mlist):
            for b in mlist[:i]:
                d, _, _ = xeuclid(a,b)
                if d != 1: raise Exception("Not coprime") 
        # Chinese remainder solving, for coprime moduli
        N = reduce(lambda x1, x2: x1*x2[1], buslist, 1) # Product of all moduli (bus periods)
        x = 0 # Initialize common solution
        for k, bus in enumerate(buslist):
            a, m = bus # a is the departure offset, m the periodicity, for each bus line
            _, x1, _ = xeuclid(N//m, m) # Solve x1*N//m % m == 1
            x += x1*(-a)*N//m # Add solution to x*N//m % m == -a to common solution
            x = x % N # reduce partial solution modulo n
        if [None for bus in buslist if (x+bus[0]) % bus[1] != 0]: # Check. Empty list if correct solution. 
            raise Exception("Not a correct solution!")
        return(x)
        
print(partone("input.txt"), parttwo("input.txt"))
