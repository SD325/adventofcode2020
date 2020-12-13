def wait(x):
    return valid_ids[x] - N % valid_ids[x]


# Source: https://github.com/kresimir-lukin/AdventOfCode2020/blob/main/helpers.py
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# Source: https://github.com/kresimir-lukin/AdventOfCode2020/blob/main/helpers.py
def chinese_remainder(n, a):
    sum_ = 0
    prod = 1
    for xx in n:
        prod *= xx
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum_ += a_i * mul_inv(p, n_i) * p
    return sum_ % prod


with open("inputs/day13.txt") as f:
    N = int(f.readline().strip())
    ids = f.readline().strip().split(',')
    valid_ids = [int(i) for i in ids if i != 'x']
    min_idx = min(range(len(valid_ids)), key=wait)  # --> argmax(t in valid_ids) wait(t)
    print(valid_ids[min_idx] * wait(min_idx))

    mods = [int(i) - idx for idx, i in enumerate(ids) if i != 'x']
    print(chinese_remainder(valid_ids, mods))
