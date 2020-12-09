""" Advent of Code 2020, day 9."""
__author__ = "Stefan Karlsson"
__date__ = "2020-12-09"

def read(f): 
    """Read lines from file and make a list."""
    return [int(line.strip()) for line in f]

def check(nlist, k):
    '''Check if number k is a sum of any two numbers in nlist.'''
    for i, num1 in enumerate(nlist):
        for num2 in nlist[i+1:]:
            if k == num1 + num2:
                return True
    return False

def check_all(code, n):
    '''Check all numbers after the preamble.'''
    for k in range (n, len(code)):
        if not check(code[k-n:k], code[k]):
            return (k, code[k])
    return True

def parttwo(code, num):
    for k, ck in enumerate(code):
        sum = ck
        for m in range(1,k):
            sum += code[k-m]
            if sum == num:
                return(k,m,min(code[k-m:k+1])+max(code[k-m:k+1]))
    return False


"""Start!"""
with open("input.txt") as f: 
    code = read(f)

ch = check_all(code, 25)
print(ch)
print(parttwo(code,ch[1]))


