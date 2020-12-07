from re import sub


def p1(ins, col):
    ret = set()
    queue = [col]
    while len(queue) > 0:
        col = queue.pop(0)
        if col not in ins:
            continue
        ret = ret.union(ins[col])
        queue.extend(list(ins[col]))
    return len(ret)


def p2(contains, col):
    if col not in contains:
        return 0
    return sum(v + v * p2(contains, c) for c, v in contains[col])


with open("inputs/day7.txt") as f:
    contain = {}
    inside = {}
    for line in f.readlines():
        x, y = tuple(line.strip().split('contain'))
        a = sub(f'bag.*', '', x.strip()).strip()
        b = y.strip().replace('.', '').split(', ')

        if len(b) == 1 and 'no other bags' in b:
            continue
        if a not in contain:
            contain[a] = []
        for _ in b:
            count = int(sub(r'\D', '', _))
            bag = sub(f'bag.*', '', sub(r'\d+', '', _)).strip()
            if bag not in inside:
                inside[bag] = set()
            inside[bag].add(a)
            contain[a].append((bag, count))

    print(p1(inside, 'shiny gold'))
    print(p2(contain, 'shiny gold'))
