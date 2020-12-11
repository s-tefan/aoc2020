""" Advent of Code 2020, day 11."""
__author__ = "Stefan Karlsson"
__date__ = "2020-12-11"

class WaitingArea:
    def __init__(self):
        self.changed = True

    def set(self, seats):
        self.seats = seats
        self.rows = len(seats)
        self.cols = len(seats[0])
        self.changed = True

    def read(self, f):
        self.seats = [line.strip() for line in f]
        self.changed = True
        self.rows, self.cols = len(self.seats), len(self.seats[0])

    def __str__(self):
        return "\n".join(self.seats)
    
    @staticmethod
    def newseat(seat, occupied):
        if seat == "L" and occupied == 0:
            return "#"
        elif seat == "#" and occupied >= 4:
            return "L"
        else:
            return seat

    @staticmethod
    def newseat2(seat, occupied):
        if seat == "L" and occupied == 0:
            return "#"
        elif seat == "#" and occupied >= 5:
            return "L"
        else:
            return seat

    def n_of_occupied(self):
        return "".join(self.seats).count("#")

    def update(self):
        newseats = []
        # first row
        seat = self.seats[0][0]
        newseatsrow = self.newseat(seat, (self.seats[0][1]+self.seats[1][:2]).count('#')) # first seat
        for j in range(1, self.cols - 1):
            seat = self.seats[0][j]
            newseatsrow += self.newseat(seat, "".join([self.seats[0][j-1], self.seats[0][j+1], self.seats[1][j-1:j+2]]).count('#'))       
        seat = self.seats[0][-1]
        newseatsrow += self.newseat(seat, (self.seats[0][-2]+self.seats[1][-2:]).count('#'))  # last seat
        newseats.append(newseatsrow)
        # following rows    
        for i in range(1, self.rows - 1):
            seat = self.seats[i][0]
            newseatsrow = self.newseat(seat, (self.seats[i-1][0:2] + self.seats[i][1] + self.seats[i+1][0:2]).count('#'))    
            for j in range(1, self.cols - 1):
                seat = self.seats[i][j]
                neighbours = "".join([self.seats[i-1][j-1:j+2], self.seats[i][j-1], self.seats[i][j+1], self.seats[i+1][j-1:j+2]])
                newseatsrow += self.newseat(seat, neighbours.count('#'))
            seat = self.seats[i][-1]
            newseatsrow += self.newseat(seat, (self.seats[i-1][-2:] + self.seats[i][-2] + self.seats[i+1][-2:]).count('#'))
            newseats.append(newseatsrow)
        # last row
        seat = self.seats[-1][0]
        newseatsrow = self.newseat(seat, (self.seats[-1][1]+self.seats[-2][:2]).count('#')) # first seat
        for j in range(1, self.cols - 1):
            seat = self.seats[-1][j]
            newseatsrow += self.newseat(seat, "".join([self.seats[-1][j-1], self.seats[-1][j+1], self.seats[-2][j-1:j+2]]).count('#'))
        seat = self.seats[-1][-1]
        newseatsrow += self.newseat(seat, (self.seats[-1][-2]+self.seats[-2][-2:]).count('#'))  # last seat
        newseats.append(newseatsrow)
        self.changed = newseats != self.seats
        self.seats = newseats


    def n_of_neighbours(self, i, j):
        d = {(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)}
        s = sum(self.seats[i+di][j+dj] == "#" for di, dj in d if 
            i+di in range(self.rows) and j+dj in range(self.cols))
        return s

    def update1(self):
        '''New version inspired by part 2. update() faster, though'''
        newseats = []
        for i in range(self.rows):
            newseatsrow = ""
            for j in range(self.cols):
                newseatsrow += self.newseat(self.seats[i][j], self.n_of_neighbours(i, j))
            newseats.append(newseatsrow)
        self.changed = newseats != self.seats
        self.seats = newseats

    def occupied_in_ray(self, i, j, di, dj):
        while True:
            i += di
            j += dj
            if (not i in range(self.rows)) or (not j in range(self.cols)):
                return False
            else:
                if self.seats[i][j] == "#":
                    return True
                elif self.seats[i][j] == "L":
                    return False

    def n_of_seen_occ(self, i, j):
        d = {(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)}
        s = sum(self.occupied_in_ray(i, j, di, dj) for di, dj in d)
        return s


    def update2(self):
        newseats = []
        for i in range(self.rows):
            newseatsrow = ""
            for j in range(self.cols):
                newseatsrow += self.newseat2(self.seats[i][j], self.n_of_seen_occ(i, j))
            newseats.append(newseatsrow)
        self.changed = newseats != self.seats
        self.seats = newseats

wa = WaitingArea()
with open("input.txt") as f: 
    wa.read(f)

while(wa.changed):
    wa.update()
print(wa.n_of_occupied())

wa = WaitingArea()
with open("input.txt") as f: 
    wa.read(f)

while(wa.changed):
    wa.update2()
print(wa.n_of_occupied())



