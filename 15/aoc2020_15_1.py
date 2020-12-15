input = [0,6,1,7,2,19,20]
test = [0,3,6]

def build(nlist, max):
    while len(nlist) < max:
        try:
            nlist.insert(0, nlist[1:].index(nlist[0]) + 1 )
        except:
            nlist.insert(0, 0)
    return nlist

ll = test.copy()
ll.reverse()
print(build(ll, 10))
ll = input.copy()
ll.reverse()
print(build(ll, 2020)[0])
