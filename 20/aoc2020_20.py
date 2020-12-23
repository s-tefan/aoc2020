class Tile:
    def __init__(self, tilerows, tileid=None):
        self.tileid = tileid
        self.tilerows = tilerows
        self.rotation = 0
        self.flipped = False

    def __repr__(self):
        return self.str(rot=self.rotation, flip=self.flipped)

    def str(self, rot=0, flip=False):
        s = "Tile {}, rotation {}, {}:\n". format(
            self.tileid,
            self.rotation,
            "flipped" if self.flipped else "not flipped")
        for k, row in enumerate(self.tilerows):
            s += self.floptop(row=k, rot=self.rotation,
                              flip=self.flipped) + "\n"
        s += "\n"
        return s

    def append(self, row):
        self.tilerows.append(row)

    def reset(self):
        self.rotation = 0
        self.flipped = False

    def floptop(self, row=0, rot=0, flip=False):
        if rot == 0:
            s = self.tilerows[row]
        elif rot == 1:
            s = "".join(r[-1-row] for r in self.tilerows)
        elif rot == 2:
            s = self.tilerows[-1-row][::-1]
        elif rot == 3:
            s = "".join(r[row] for r in reversed(self.tilerows))
        if flip:
            s = s[::-1]
        return s

    def top(self):
        return self.floptop(rot=self.rotation, flip=self.flipped)

    def bottom(self):
        return self.floptop(row=-1, rot=self.rotation, flip=self.flipped)

    def rotate(self, n=1):
        self.rotation += n
        self.rotation %= 4

    def flip(self, how=-1):
        if how == -1:
            self.flipped = not self.flipped
        else:
            self.flipped = How


def gettiles(filename):
    tiles = {}
    tileid = None
    with open(filename) as f:
        for line in f:
            stripline = line.strip(" \n\r")
            if stripline[:4].lower() == "tile":
                tileid = int(stripline[4:].strip(" :"))
                tiles[tileid] = Tile(tileid=tileid, tilerows=[])
            elif stripline:
                tiles[tileid].append(stripline)
    return tiles


def get_below(first, tiles):
    bot = first.bottom()
    for tileid, tile in tiles.items():
        for flip in (False, True):
            for k in range(4):
                if bot == tile.floptop(rot=k, flip=flip):
                    tiles.pop(tileid)
                    tile.rotation = k
                    tile.flipped = flip
                    return tile
    return None


def partone(filename, verbose=False):
    tiles = gettiles(filename)
    firstid, first = tiles.popitem()
    if verbose:
        print(first)
    last = first
    # Get down to the bottom
    while below := get_below(last, tiles):
        if verbose:
            print(below)
        last = below
    if verbose:
        print("Find the corners.")
    if True:
        remember = last  # At bottom
        if verbose:
            print("Rotate and go down, for going right.")
        last.rotate()
        if verbose:
            print(last)
        while aside := get_below(last, tiles):
            if verbose:
                print('->', aside)
            last = aside
        bottomright = last
        if verbose:
            print("Rotate and go down, for going left.")
        if verbose:
            print(last)
        last = remember  # Just remember it has been rotated
        last.rotate(-2)
        while aside := get_below(last, tiles):
            if verbose:
                print('<-', aside)
            last = aside
        bottomleft = last
    # Get up to the top
    last = first
    last.reset()
    last.rotate(2)
    while below := get_below(last, tiles):
        if verbose:
            print(below)
        last = below
    if verbose:
        print("Find the corners.")
    if True:
        remember = last  # At bottom
        if verbose:
            print("Rotate and go down, for going right.")
        last.rotate(1)
        if verbose:
            print(last)
        while aside := get_below(last, tiles):
            if verbose:
                print('->', aside)
            last = aside
        topright = last
        if verbose:
            print("Rotate and go down, for going left.")
        if verbose:
            print(last)
        last = remember  # Just remember it has been rotated
        last.rotate(2)
        while aside := get_below(last, tiles):
            if verbose:
                print('<-', aside)
            last = aside
        topleft = last
    p = 1
    for corner in {bottomright, bottomleft, topright, topleft}:
        p *= corner.tileid

    if verbose:
        print("Bottom right:\n{}Bottom left:\n{}Top right:\n{}Top left:\n{}".format(
            bottomright, bottomleft, topright, topleft))
        print("Product of corner id:s: {}".format(p))
    return p


print("Part one, test.txt:", partone("test.txt"))
print("Part one, input.txt:", partone("input.txt"))
