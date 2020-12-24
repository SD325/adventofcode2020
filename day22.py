def combat(plyr1, plyr2):
    while plyr1 and plyr2:
        c1, c2 = plyr1.pop(0), plyr2.pop(0)
        if c1 > c2:
            plyr1.append(c1)
            plyr1.append(c2)
        else:
            plyr2.append(c2)
            plyr2.append(c1)
    return sum((i + 1) * v for i, v in enumerate(plyr1[::-1] or plyr2[::-1]))


def recursive_combat(plyr1, plyr2, isGame1=False):
    visited = set()
    while plyr1 and plyr2:
        curr = (tuple(plyr1), tuple(plyr2))
        if curr in visited:
            return True
        visited.add(curr)
        c1, c2 = plyr1.pop(0), plyr2.pop(0)
        if recursive_combat(plyr1[:c1], plyr2[:c2]) if len(plyr1) >= c1 and len(plyr2) >= c2 else c1 > c2:
            plyr1.append(c1)
            plyr1.append(c2)
        else:
            plyr2.append(c2)
            plyr2.append(c1)
    return sum((i + 1) * v for i, v in enumerate(plyr1[::-1] or plyr2[::-1])) if isGame1 else len(plyr1) > 0


with open("inputs/day22.txt") as f:
    inp = [l.strip() for l in f.readlines()]
    player1 = [int(ii) for ii in inp[1:inp.index('Player 2:')-1]]
    player2 = [int(ii) for ii in inp[inp.index('Player 2:')+1:]]
    print(combat(player1[:], player2[:]))
    print(recursive_combat(player1[:], player2[:], isGame1=True))
