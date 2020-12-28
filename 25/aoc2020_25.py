def mlog(x, base, modulo):
    """ Return the base logarithm of x modulo modulo. """
    # the crude way
    m = 1
    y = 0
    while m != x:
        m *= base
        m %= modulo
        y += 1
    return y


def mpow(x, n, modulo):
    """ Return the nth power of x modulo modulo. """
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2:  # odd power
        return (x * mpow(x, n // 2, modulo) ** 2) % modulo
    else:  # even power
        return (mpow(x, n // 2, modulo) ** 2) % modulo


def test():
    pubkey1 = 5764801
    pubkey2 = 17807724
    subnum = 7
    cmod = 20201227
    return mpow(pubkey2, mlog(pubkey1, subnum, cmod), cmod)


def partone(filename):
    with open(filename) as f:
        pubkey1 = int(f.readline())
        pubkey2 = int(f.readline())
    subnum = 7
    cmod = 20201227
    return mpow(pubkey2, mlog(pubkey1, subnum, cmod), cmod)


print(test())
print(partone('input.txt'))
