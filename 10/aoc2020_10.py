from math import comb
from time import time

def diffs(ll):
    return [a - b for a, b in zip(ll[1:], ll[:-1])]


class AdapterList:
    def read(self, f):
        self.alist = sorted([int(line.strip()) for line in f])
    def diffs(self):
        ll = [0] + self.alist + [self.alist[-1] + 3]
        return diffs(ll)
def rec_count(blist):
    #print(blist)
    if len(blist) == 2:
        if blist[1]-blist[0] == 3:
            #print("*")
            return 1
        else:
            raise Exception("Nåt fel")
    elif len(blist) == 3:
        if blist[2]-blist[0] <= 3:
            return rec_count(blist[1:] + rec_count(blist[2:]))
        else:
            return rec_count(blist[1:])
    elif len(blist) >= 4:
        if blist[2]-blist[0] <= 3:
            return rec_count(blist[1:]) + rec_count(blist[2:])
        else:
            return rec_count(blist[1:])
    else:
        raise Exception("För kort lista")

def rec_count_diff(difflist):
    if len(difflist) <= 2:
        return 1
    elif difflist[0] + difflist[1] <=3:
        s = difflist[0] + difflist[1]
        return rec_count_diff(difflist[1:]) + rec_count_diff([s] + difflist[2:])
    else:
        return rec_count_diff(difflist[1:])


def partitions_of_ones(n):
    sum = 0
    for k in range(n//3): #number of threes
        for m in range((n-k)//2):
            sum += comb(n-2*k, k) * comb(n-2*k-m, m)
    return sum

def pupp(n):
    if n <= 1:
        return 1
    elif n <= 2:
        return pupp(n-1) + pupp(n-2)
    elif n >= 3:
        return pupp(n-1) + pupp(n-2) + pupp(n-3)
    else: 
        pass

def one_seqs(ll):
    n_of_1 = 0
    n_of_1_list = []
    combs = 1
    for num in ll:
        if num == 1:
            n_of_1 +=1
        elif num == 3:
            if n_of_1 >0:
                n_of_1_list.append(n_of_1)
                combs *= pupp(n_of_1)
            n_of_1 = 0
    return combs, n_of_1_list
    
        


with open("input.txt") as f: 
    adapterlist = AdapterList()
    adapterlist.read(f)
difflist = adapterlist.diffs()
print(difflist)
print(difflist.count(1)*difflist.count(3))
apa = adapterlist.alist
#apa = [1,2,3,4]
'''
print("time: {}",format(time()))
print(rec_count([0]+apa+[apa[-1]+3]))
print("time: {}",format(time()))
difflist = diffs([0]+apa+[apa[-1]+3])
print(rec_count_diff(difflist))
'''
print("time: {}",format(time()))
print(one_seqs(difflist))

