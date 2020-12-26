""" Advent of Code 2020, day 10."""
__author__ = "Stefan Karlsson"
__date__ = "2020-12-10"

def diffs(ll):
    return [a - b for a, b in zip(ll + [ll[-1]+3], [0] + ll) ]

def read(f):
    return sorted([int(line.strip()) for line in f])

def pupp(n):
    '''Count the number of compositions of n with terms 1, 2 or 3.'''
    if n <= 1:
        return 1
    elif n <= 2:
        return pupp(n-1) + pupp(n-2)
    elif n >= 3:
        return pupp(n-1) + pupp(n-2) + pupp(n-3)
    else: 
        pass

def parttwo(ll):
    '''Find seqs of 1:s and feed # to pupp. Multiply.'''
    n_of_1 = 0
    combs = 1
    for num in ll:
        if num == 1:
            n_of_1 +=1
        elif num == 3:
            if n_of_1 >0:
                combs *= pupp(n_of_1)
            n_of_1 = 0
        else:
            raise Exception("Other diffs than 1 or 3 in data")
    return combs
    
with open("input.txt") as f: 
    difflist = diffs(read(f))
print(difflist.count(1)*difflist.count(3))
print(parttwo(difflist))

