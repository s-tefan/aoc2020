
def count_valid_1(filename):
    with open(filename) as f:
        input = f.readlines()
    #print(len(input))
    valids = [check(split_line(line)) for line in input]
    return sum(valids)

def count_valid_2(filename):
    with open(filename) as f:
        input = f.readlines()
    valids = [check_2(split_line(line)) for line in input]
    return sum(valids)

def split_line(s):
    sl1 = s.split()
    sl2 = sl1[0].split('-')
    return {
        'min': int(sl2[0]), 
        'max': int(sl2[1]), 
        'char': sl1[1][0],
        'passwd': sl1[2] }

def check(record):
    n = record['passwd'].count(record['char'])
    return record['min'] <= n and n <= record['max']

def check_2(record):
    passwd = record['passwd']
    c = record['char']
    test = (passwd[record['min']-1]==c) != (passwd[record['max']-1]==c)
    #print(test, c, passwd, record['min'], record['max'], passwd[record['min']-1], passwd[record['max']-1])
    return test

print(count_valid_1("input.txt"))
print(count_valid_2("input.txt"))
