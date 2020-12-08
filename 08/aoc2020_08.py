""" Advent of Code 2020, day 8."""
__author__ = "Stefan Karlsson"
__date__ = "2020-12-08"

def read(f): 
    """Read lines from file and make a corresponding list of dicts."""
    code = []
    for line in f:
        instr, num_str = line.strip().split(" ") 
        code.append({"instr":instr, "num": int(num_str), "runs": 0})
    return code

def run(code):
    pos = 0
    acc = 0
    while pos < len(code) and code[pos]["runs"] == 0:
        code[pos]["runs"] += 1
        codeline = code[pos]
        #print("{}: {}".format(pos, codeline))
        if codeline["instr"] == "acc":
            acc += codeline["num"]
            pos += 1
        elif codeline["instr"] == "jmp":
            pos += codeline["num"]
        elif codeline["instr"] == "nop":
            pos += 1
        else: raise Exception("Unknown code at line {}!", pos)
    #print("last: {}".format(code[pos]))
    return {"finished": pos >= len(code), "acc": acc, "pos": pos}

def halfdeepcopy(l):
    '''Make a list where every element is copied.'''
    return [elem.copy() for elem in l]

def two(code):
    for k, line in enumerate(code):
        if line["instr"] == "nop":
            c = halfdeepcopy(code)
            c[k]["instr"] = "jmp"
        elif line["instr"] == "jmp":
            c = halfdeepcopy(code)
            c[k]["instr"] = "nop"
        ret = run(c)
        if ret["finished"]:
            return ret, k

"""Start!"""
with open("input.txt") as f: 
    code = read(f)
print(run(halfdeepcopy(code)))
print(two(code))
