def bitmask(v):
    res = list(mask[::-1])
    rev_string = str(bin(v))[2:][::-1]
    for i, x in enumerate(rev_string):
        res[i] = x if mask[len(mask) - i - 1] == 'X' else mask[len(mask) - i - 1]
    res = ['0' if x == 'X' else x for x in res]
    return int(''.join(res[::-1]), 2)


with open("inputs/day14.txt") as f:
    mem, mask = {}, ''
    for line in f.readlines():
        if line[:3] == 'mem':
            address = int(line[line.index('[')+1:line.index(']')])
            value = int(line[line.index('=')+1:].strip())
            mem[address] = bitmask(value)
        else:
            mask = line[line.index('=')+1:].strip()
    print(sum(mem.values()))
