def p1_check(a, i, j, dr, dc):
    return 0 <= i+dr < len(a) and 0 <= j+dc < len(a[0]) and a[i+dr][j+dc] == '#'


def p2_check(a, i, j, dr, dc):
    step = 1
    while 0 <= i+dr*step < len(a) and 0 <= j+dc*step < len(a[0]):
        curr = a[i+dr*step][j+dc*step]
        if curr == '#':
            return True
        elif curr == 'L':
            return False
        step += 1
    return False


def process(a, check, MIN_REQ):
    seats = [list(xx) for xx in a]
    changed = False
    ADJ = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 'L' and all(not check(a, i, j, dr, dc) for dr, dc in ADJ):
                seats[i][j] = '#'
                changed = True
            elif a[i][j] == '#' and sum(check(a, i, j, dr, dc) for dr, dc in ADJ) >= MIN_REQ:
                seats[i][j] = 'L'
                changed = True
    return process(seats, check, MIN_REQ) if changed else sum(s.count('#') for s in seats)


with open("inputs/day11.txt") as f:
    inp = [list(l.strip()) for l in f.readlines()]
    print(process(inp, p1_check, 4))
    print(process(inp, p2_check, 5))
