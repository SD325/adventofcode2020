def p1(a):
    x = y = 0
    facing = 0
    for act, step in a:
        if act == 'N':
            y += step
        elif act == 'S':
            y -= step
        elif act == 'E':
            x += step
        elif act == 'W':
            x -= step
        elif act == 'L':
            facing += step // 90
            facing %= 4
        elif act == 'R':
            facing -= step // 90
            facing %= 4
        elif act == 'F':
            if facing % 2 == 0:
                x += step if facing == 0 else (-step)
            else:
                y += step if facing == 1 else (-step)
    return abs(x) + abs(y)


def turn(step, w_x, w_y):
    if step == 90:
        return -w_y, w_x
    elif step == 180:
        return -w_x, -w_y
    elif step == 270:
        return w_y, -w_x
    return None


def p2(a):
    x = y = 0
    w_x, w_y = 10, 1
    for act, step in a:
        if act == 'N':
            w_y += step
        elif act == 'S':
            w_y -= step
        elif act == 'E':
            w_x += step
        elif act == 'W':
            w_x -= step
        elif act == 'L':
            w_x, w_y = turn(step, w_x, w_y)
        elif act == 'R':
            w_x, w_y = turn(-step % 360, w_x, w_y)
        elif act == 'F':
            x += step * w_x
            y += step * w_y
    return abs(x) + abs(y)


with open("inputs/day12.txt") as f:
    inp = [(l.strip()[0], int(l.strip()[1:])) for l in f.readlines()]
    print(p1(inp))
    print(p2(inp))
