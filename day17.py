def get_neighbors_p1(cube):
    return [(cube[0]+x, cube[1]+y, cube[2]+z)
            for x in range(-1, 2)
            for y in range(-1, 2)
            for z in range(-1, 2)
            if not x == y == z == 0]


def get_neighbors_p2(cube):
    return [(cube[0]+w, cube[1]+x, cube[2]+y, cube[3]+z)
            for w in range(-1, 2)
            for x in range(-1, 2)
            for y in range(-1, 2)
            for z in range(-1, 2)
            if not w == x == y == z == 0]


def conway(cubes, get_neighbors):
    for cycle in range(6):
        for n in [n for c in cubes for n in get_neighbors(c)]:
            cubes.setdefault(n, False)
        new_cubes = {}
        for c, v in cubes.items():
            n_on = sum(cubes[n] for n in get_neighbors(c) if n in cubes)
            new_cubes[c] = True if n_on == 3 or (v and n_on == 2) else False
        cubes = new_cubes
    return sum(cubes.values())


with open("inputs/day17.txt") as f:
    inp = [ll.strip() for ll in f.readlines()]
    print(conway({(i, j, 0): (s == '#') for i, l in enumerate(inp) for j, s in enumerate(l)}, get_neighbors_p1))
    print(conway({(i, j, 0, 0): (s == '#') for i, l in enumerate(inp) for j, s in enumerate(l)}, get_neighbors_p2))
