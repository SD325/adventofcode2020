def isOcc(a, r, c):
    return 0 <= r < len(a) and 0 <= c < len(a[0]) and a[r][c] == '#'


def p1(a):
    seats = [list(xx) for xx in a]
    changed = False
    adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 'L' and all(not isOcc(a, i+dr, j+dc) for dr, dc in adj):
                seats[i][j] = '#'
                changed = True
            elif a[i][j] == '#' and sum(isOcc(a, i+dr, j+dc) for dr, dc in adj) >= 4:
                seats[i][j] = 'L'
                changed = True
    return p1(seats) if changed else sum(s.count('#') for s in seats)


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



def p2(a):
    seats = [list(xx) for xx in a]
    changed = False
    adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 'L' and all(not p2_check(a, i, j, dr, dc) for dr, dc in adj):
                seats[i][j] = '#'
                changed = True
            elif a[i][j] == '#' and sum(p2_check(a, i, j, dr, dc) for dr, dc in adj) >= 5:
                seats[i][j] = 'L'
                changed = True
    return p2(seats) if changed else sum(s.count('#') for s in seats)


with open("inputs/day11.txt") as f:
    inp = [list(l.strip()) for l in f.readlines()]
    print(p1(inp))
    print(p2(inp))
