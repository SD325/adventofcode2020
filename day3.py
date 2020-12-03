def p1(a):
    tree_count = 0
    num_r, num_c = len(a), len(a[0])
    c = 0
    for r in range(num_r):
        if a[r][c] == '#':
            tree_count += 1
        c += 3
        c %= num_c
    return tree_count


def p2(a, delta_r, delta_c):
    prod_trees = 1
    num_r, num_c = len(a), len(a[0])
    for d_r, d_c in zip(delta_r, delta_c):
        tree_count = 0
        c = 0
        for r in range(0, num_r, d_r):
            if a[r][c] == '#':
                tree_count += 1
            c += d_c
            c %= num_c
        prod_trees *= tree_count
    return prod_trees


with open("inputs/day3.txt") as f:
    arr = [list(x) for line in f for x in line.split()]
    print(p1(arr))
    print(p2(arr, [1, 1, 1, 1, 2], [1, 3, 5, 7, 1]))
