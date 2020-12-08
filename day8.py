def execute(a):
    acc = itr = 0
    visited = set()
    while True:
        if itr in visited:
            return acc, False
        if itr == len(a):
            return acc, True
        visited.add(itr)
        acc += a[itr][1] if a[itr][0] == 'acc' else 0
        itr += a[itr][1] if a[itr][0] == 'jmp' else 1


def p2(a):
    for i, (arg, _) in enumerate(a):
        if arg == 'acc':
            continue
        res, fixed = execute(a[:i] + [('jmp', a[i][1])] + a[i+1:]) if arg == 'nop' \
            else execute(a[:i] + [('nop', a[i][1])] + a[i+1:])
        if fixed:
            return res


with open("inputs/day8.txt") as f:
    ins = [(l.split()[0], int(l.split()[1])) for l in f.readlines()]
    print(execute(ins)[0])
    print(p2(ins))
