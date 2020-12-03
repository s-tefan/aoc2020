//  aoc2020_01.cs
/*
with open("input01.txt") as f:
    input = f.readlines()

numlist = [int(s) for s in input]
sum_wanted = 2020

def check2(nlist, sum):
    for k in range(len(numlist)):
        for j in range(k):
            if numlist[k] + numlist[j] == sum_wanted:
                return(numlist[k],numlist[j])
    return None
*/
public int[][] check2(int[] nlist, int sum )
{
    for (int k = 0; k < len(nlist); k++) {
        Console.WriteLine(k);
    }
    return [[0]];

}

/*
def check3(nlist, sum):
    for k in range(len(numlist)):
        for j in range(k):
            for i in range(j):
                if numlist[k] + numlist[j] + numlist[i] == sum_wanted:
                    return(numlist[k],numlist[j],numlist[i])
    return None


pair = check2(numlist, sum_wanted)
triple = check3(numlist, sum_wanted)
            
print(pair[0]*pair[1])
print(triple[0]*triple[1]*triple[2])
*/
static void Main(string[] args)
{
    int[][] ap = check([3,2,1], 5)
}

Console.WriteLine("Hello World!");