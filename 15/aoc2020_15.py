input = [0,6,1,7,2,19,20]
test = [0,3,6]

def build2(startlist, max):
    '''Store each number with its last position in a dict. Return last number.'''
    pos = len(startlist)
    d = {}
    for k, n in enumerate(startlist[:-1]):
        d[n] = k + 1
    last = startlist[-1]
    while pos < max :
        #print(pos, d, last) 
        lastpos = d.get(last)
        if lastpos == None:
            d[last] = pos
            last = 0
        else:
            d[last] = pos
            last =  pos - lastpos
        pos += 1
    return last, len(d)

import time
tstack=[]
tstack.append(time.process_time())
print(build2(test, 2020))
tstack.append(time.process_time())
print("Time: {}".format(tstack.pop()-tstack.pop()))
tstack.append(time.process_time())
print(build2(input, 2020))
tstack.append(time.process_time())
print("Time: {}".format(tstack.pop()-tstack.pop()))
tstack.append(time.process_time())
print(build2(input, 30000000))
tstack.append(time.process_time())
print("Time: {}".format(tstack.pop()-tstack.pop()))


