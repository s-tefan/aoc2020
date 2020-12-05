def bin_sub(c):
    if c in 'FfLl': 
        return '0'
    elif c in 'BbRr': 
        return '1'
    else: 
        raise Exception("Syntax error in file")

def one():
    filename = "input.txt"
    min, max = None, 0
    with open(filename) as f:
        for line in f: 
            a = int("".join([bin_sub(c) for c in line.strip()]), 2)
            if a > max:
                max = a
            if min == None or a < min:
                min = a
    return min, max

def one_var():
    filename = "input.txt"
    with open(filename) as f:
        return max(int("".join([bin_sub(c) for c in line.strip()]), 2) for line in f)

def two():
    filename = "input.txt"
    min, max = one() 
    bp_set = set({})
    with open(filename) as f:
        for line in f: 
            bp_set.add(int("".join([bin_sub(c) for c in line.strip()]), 2))
    return set(range(min+1,max)) - bp_set

print(one()[1])
print(one_var())
print(two())

