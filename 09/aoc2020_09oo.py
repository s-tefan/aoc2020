""" Advent of Code 2020, day 9. OO version"""
__author__ = "Stefan Karlsson"
__date__ = "2020-12-09"

class XMAS:
    def set_preamble_size(self, n):
        self.preamble_size = n

    def read(self, f): 
        """Read lines from file into object variable code."""
        self.code = [int(line.strip()) for line in f]

    def check(self, nlist, k):
        '''Check if number k is a sum of any two numbers in nlist.'''
        for i, num1 in enumerate(nlist):
            for num2 in nlist[i+1:]:
                if k == num1 + num2:
                    return True
        return False

    def check_all(self):
        '''Check all numbers after the preamble.'''
        n = self.preamble_size
        for k in range (n, len(self.code)):
            if not self.check(self.code[k-n:k], self.code[k]):
                return (k, self.code[k])
        return True

    def parttwo(self, num):
        for k, ck in enumerate(self.code):
            sum = ck
            for m in range(1,k):
                sum += self.code[k-m]
                if sum == num:
                    return(k,m,min(self.code[k-m:k+1])+max(self.code[k-m:k+1]))
        return False

"""Start!"""
xmas = XMAS()
xmas.set_preamble_size(25)
with open("input.txt") as f: 
    xmas.read(f)

ch = xmas.check_all()
print(ch)
print(xmas.parttwo(ch[1]))
