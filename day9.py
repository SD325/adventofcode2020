def p1(a):
    for i in range(25, len(a)):
        all_sums = set(a[x]+a[y] for x in range(i-25, i) for y in range(x+1, i))
        if a[i] not in all_sums:
            return a[i]
    return -1


def p2(a, n):
    prefix = [sum(a[:x+1]) for x in range(len(a))]
    for win in range(2, len(a)):
        for i in range(len(a) - win):
            if prefix[i+win] - prefix[i] == n:
                return max(a[i+1:i+win+1]) + min(a[i+1:i+win+1])


with open("inputs/day9.txt") as f:
    inp = [int(l.strip()) for l in f.readlines()]
    p1_ = p1(inp)
    print(p1_)
    print(p2(inp, p1_))
