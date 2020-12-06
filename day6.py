with open("inputs/day6.txt") as f:
    a = [x.replace('\n', ' ').strip() for x in f.read().split("\n\n")]
    print(sum([len(set.union(*[set(p) for p in g.split()])) for g in a]))
    print(sum([len(set.intersection(*[set(p) for p in g.split()])) for g in a]))
