with open("inputs/day10.txt") as f:
    inp = [0] + sorted([int(l.strip()) for l in f.readlines()])
    inp.append(inp[-1] + 3)

    diffs = [inp[x] - inp[x - 1] for x in range(1, len(inp))]
    print(diffs.count(1) * diffs.count(3))

    mem = [1]
    for n in range(1, len(inp)):
        mem.append(0)
        for i in range(1, 4):
            if n-i >= 0 and inp[n] - inp[n-i] <= 3:
                mem[-1] += mem[n-i]
    print(mem[-1])
